from django.shortcuts import render
from django.views import generic
from django.shortcuts import get_object_or_404
from django.http import HttpResponse

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
    car_class = get_object_or_404(CarClass, pk=pk)
    brand = car_class.car_class.all()
    return render(request, 'pages/car_show_by_brand.html', {'car_sub': brand})


# class CarShow(generic.DetailView):
#     template_name = 'pages/car_show.html'
#     model = Car,Comment
#     context_object_name = ['car','comment_form','comment']

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data()
    #     context['comment'] = lazy(get_object_or_404(Comment)


def car_show(request, pk, **kwargs):
    car = Car.objects.all()
    comment = Comment.objects.all()

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if request.user.is_authenticated:
            print('1 ok')
            Comment.objects.create(car=car,author=request.user.id)

            if comment_form.is_valid():
                print('2 ok ')
                # comment_form.author = request.user.id
                # comment_form.car = Car.objects.get(pk=pk).id
                comment_form.save()
                comment_form = CommentForm()
                return render(request, 'pages/car_show.html',
                      {'comment_from': comment_form,'car': car, 'comment': comment, })
            else:
                return render(request, 'pages/car_show.html',
                      {'comment_form': comment_form,'car': car, 'comment': comment, })
        else:
            return HttpResponse("access denied")

    else:
        comment_form = CommentForm()
        return render(request, 'pages/car_show.html',
                      {'comment_form': comment_form,'car': car, 'comment': comment, })
