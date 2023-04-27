from django.urls import path
from . views import HomePage,car_brand,car_show,car_brand_subset

app_name = 'pages'

urlpatterns = [

    path('', HomePage.as_view(), name='home'),
    path('<int:pk>/', car_brand,name='show_by_brand'),
    path('<int>/<int:pk>/', car_brand_subset, name='car_brand_subset'),
    path('<int>/<num>/<int:pk>/', car_show, name='car_show'),

]

