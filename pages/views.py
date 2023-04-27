from django.shortcuts import render
from django.views import generic
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.shortcuts import reverse

from .models import CarClass, CarBrand, Car, Comment
from .forms import CommentForm


class HomePage(generic.ListView):
    model = CarClass
    template_name = 'pages/home.html'
    context_object_name = 'car'


# class CarClassSub(generic.ListView):
#     model = CarClassSUb
#     template_name = 'pages/car_show_by_class.html'
#     context_object_name = 'car'

def car_brand(request, pk):
    # try:
    car_class = get_object_or_404(CarClass, pk=pk)
    brand = car_class.car_class.all()
    return render(request, 'pages/car_show_by_brand.html', {'car_brand': brand})
    # finally:
    #     brand = ''
    #     return render(request, 'pages/car_show_by_brand.html', {'car_brand': brand})


def car_brand_subset(request, pk, **kwargs):
    car_brand_sub = get_object_or_404(CarBrand, pk=pk)
    car = car_brand_sub.car_brand.all()
    return render(request, 'pages/car_brand_sub.html', {'car': car})


# class CarShow(generic.DetailView):
#     template_name = 'pages/car_show.html'
#     model = Car,Comment
#     context_object_name = ['car','comment_form','comment']

# def get_context_data(self, **kwargs):
#     context = super().get_context_data()
#     context['comment'] = lazy(get_object_or_404(Comment)


def car_show(request, pk, **kwargs):
    car = get_object_or_404(Car, pk=pk)
    comment = car.car.all()
    comment_count=comment.all().count()

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if request.user.is_authenticated:
            if comment_form.is_valid():
                new_comment_form = comment_form.save(commit=False)
                new_comment_form.author = request.user
                new_comment_form.car = car
                new_comment_form.save()
                comment_form = CommentForm()
            else:
                return render(request, 'pages/car_show.html',
                              {'comment_form': comment_form, 'car': car, 'comment': comment,'comment_count':comment_count })
        else:
            return HttpResponse("access denied")

    else:
        comment_form = CommentForm()

    return render(request, 'pages/car_show.html',
                  {'comment_form': comment_form, 'car': car, 'comment': comment,'comment_count':comment_count })
