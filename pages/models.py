from django.db import models
from django.shortcuts import reverse
from django.contrib.auth import get_user_model


class CarClass(models.Model):
    title = models.CharField(max_length=100,verbose_name='car class')
    description = models.TextField(blank=True, verbose_name='description')
    image = models.ImageField(blank=True , upload_to='media/image')

    def get_absolute_url(self):
        return reverse('home')

    def __str__(self):
        return self.title


class CarBrand(models.Model):
    car_class = models.ForeignKey(CarClass, related_name='car_class', on_delete=models.CASCADE, verbose_name='car class')
    title = models.CharField(max_length=20)
    description = models.TextField(verbose_name='description' , blank=True)
    image = models.ImageField(blank=True , upload_to='media/image')

    def __str__(self):
        return self.title


class Car(models.Model):
    car_brand = models.ForeignKey(CarBrand, related_name='car_brand', on_delete=models.CASCADE, verbose_name='brand')
    title = models.CharField(max_length=200,)
    description = models.TextField(verbose_name='description', blank=True)
    image = models.ImageField(blank=True , upload_to='media/image')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('show_by_class',args={self.car_brand.car_brand.id})


class Comment(models.Model):
    author = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    car = models.ForeignKey(Car,on_delete=models.CASCADE, related_name='car')
    text = models.TextField(max_length=400, verbose_name='text')
    date_time_created = models.DateTimeField(verbose_name='date time created',auto_now_add=True)
    date_time_modified = models.DateTimeField(verbose_name='date time modified',auto_now=True,blank=True)

    def __str__(self):
        return self.text
