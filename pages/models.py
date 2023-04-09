from django.db import models
from django.shortcuts import reverse



class CarClass(models.Model):
    title = models.CharField(max_length=100,verbose_name='car class')
    description = models.TextField(blank=True, verbose_name='description')
    image = models.ImageField(blank=True , upload_to='media/image')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('show_by_class', args=[self.pk])


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