from django.shortcuts import render
from django.views import generic


from .models import CarClass


class homepage(generic.ListView):
    model = CarClass
    template_name = 'pages/home.html'
    context_object_name = 'car'



