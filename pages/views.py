from django.shortcuts import render
from django.utils.functional import lazy
from django.views import generic
from django.shortcuts import get_object_or_404


from .models import CarClass, CarBrand ,Car


class Homepage(generic.ListView):
    model = CarClass
    template_name = 'pages/home.html'
    context_object_name = 'car'


# class CarClassSub(generic.ListView):
#     model = CarClassSUb
#     template_name = 'pages/car_show_by_class.html'
#     context_object_name = 'car'

def car_brand(request, pk):
    car_class = get_object_or_404(CarClass,pk=pk)
    car_brand = car_class.car_class.all()
    return render(request, 'pages/car_show_by_brand.html', {'car_sub': car_brand})


class CarShow(generic.DetailView):
    template_name = 'pages/car_show.html'
    model = Car
    context_object_name = 'car'

    # def get_context_data(self, pk=None, **kwargs):
    #     context = super().get_context_data()
    #     context[car_brand] = lazy(get_object_or_404(CarBrand,pk=pk).car_brand.all())
