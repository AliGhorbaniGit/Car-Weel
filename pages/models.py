from django.db import models


class CarClass(models.Model):
    title = models.CharField(max_length=100,verbose_name='title')
    description = models.TextField(blank=True, verbose_name='description')


class CarClassSUb(models.Model):
    car_sub = models.ForeignKey(CarClass, max_length=100, related_name='car', on_delete=models.CASCADE, verbose_name='title')
    description = models.TextField(verbose_name='description')
