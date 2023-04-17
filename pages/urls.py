from django.urls import path
from . views import Homepage,car_brand,car_show

urlpatterns = [

    path('', Homepage.as_view(), name='home'),
    path('<int:pk>/', car_brand,name='show_by_class'),
    path('<int>/<int:pk>/',car_show, name='car_show')

]

