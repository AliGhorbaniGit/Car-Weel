from django.shortcuts import render
from django.views import generic


from .models import CarClass


class MainPage(generic.ListView):
    model = CarClass
    template_name = 'pages/car_show.html'
    context_object_name = 'car'



