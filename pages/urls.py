from django.urls import path
from . views import Homepage,car_class_sub,CarShow

urlpatterns = [

    path('', Homepage.as_view(), name='home'),
    path('<int:pk>/', car_class_sub,name='show_by_class'),
    path('<int>/<int:pk>',CarShow.as_view(), name='car_show')

]

