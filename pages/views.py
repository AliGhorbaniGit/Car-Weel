from django.shortcuts import render
from django.utils.functional import lazy
from django.views import generic
from django.shortcuts import get_object_or_404
from .forms import CommentForm
from django.http import HttpResponse

from .models import CarClass, CarBrand, Car, Comment


class Homepage(generic.ListView):
    model = CarClass
    template_name = 'pages/home.html'
    context_object_name = 'car'


# class CarClassSub(generic.ListView):
#     model = CarClassSUb
#     template_name = 'pages/car_show_by_class.html'
#     context_object_name = 'car'

def car_brand(request, pk):
    car_class = get_object_or_404(CarClass, pk=pk)
    brand = car_class.car_class.all()
    return render(request, 'pages/car_show_by_brand.html', {'car_sub': brand})


# class CarShow(generic.DetailView):
#     template_name = 'pages/car_show.html'
#     model = Car
#     context_object_name = 'car'

#     # def get_context_data(self, **kwargs):
#     #     context = super().get_context_data()
#     #     context['comment'] = lazy(get_object_or_404(Comment)


def car_show(request, pk, **kwargs):
    car = Car.objects.get(pk=pk)
    comment = car.car.all()
    comment_form = CommentForm

    if request.method == 'POST':
        if request.user.is_authenticated:
            form = CommentForm(request.POST)
            if form.is_valid():
                form.save()
                comment_form = CommentForm
            return render(request, 'pages/car_show.html',
                          {'car': car, 'comment': comment, 'comment_from': comment_form})
        else:
            return HttpResponse("hhhhhhhhh sheyton bala")


    else:
        return render(request, 'pages/car_show.html', {'car': car, 'comment': comment, 'comment_from': comment_form})
