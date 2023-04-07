from django.db import models
from django.shortcuts import reverse


class CarClass(models.Model):
    title = models.CharField(max_length=100,verbose_name='title')
    description = models.TextField(blank=True, verbose_name='description')
    image = models.ImageField(blank=True , upload_to='media/image')

    def get_absolute_url(self):
        return reverse('show_by_class', args=[self.pk])


class CarClassSUb(models.Model):
    car_sub = models.ForeignKey(CarClass, max_length=100, related_name='car', on_delete=models.CASCADE, verbose_name='sub')
    title = models.CharField(max_length=200,blank=True)
    description = models.TextField(verbose_name='description')
    image = models.ImageField(blank=True , upload_to='media/image')

