from django.urls import path
from . views import Homepage,car_brand,CarShow

urlpatterns = [

    path('', Homepage.as_view(), name='home'),
    path('<int:pk>/', car_brand,name='show_by_class'),
    path('<int>/<int:pk>',CarShow.as_view(), name='car_show')

]

