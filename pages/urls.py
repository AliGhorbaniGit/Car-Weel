from django.urls import path
from . views import HomePage,car_brand,car_show

app_name = 'pages'

urlpatterns = [

    path('', HomePage.as_view(), name='home'),
    path('<int:pk>/', car_brand,name='show_by_class'),
    path('<int>/<int:pk>/', car_show, name='car_show')

]

