from django.shortcuts import render
from django.views import generic
from django.shortcuts import get_object_or_404


from .models import CarClass, CarClassSUb


class Homepage(generic.ListView):
    model = CarClass
    template_name = 'pages/home.html'
    context_object_name = 'car'


# class CarClassSub(generic.ListView):
#     model = CarClassSUb
#     template_name = 'pages/car_show_by_class.html'
#     context_object_name = 'car'

def car_class_sub(request, pk):
    car_class = get_object_or_404(CarClass,pk=pk)
    car_sub = car_class.car.all()
    return render(request, 'pages/car_show_by_class.html', {'car_sub': car_sub})


class CarShow(generic.DetailView):
    template_name = 'pages/car_show.html'
    model = CarClassSUb
    context_object_name = 'car'



