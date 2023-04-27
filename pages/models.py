from django.db import models
from django.shortcuts import reverse
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _


class CarClass(models.Model):
    title = models.CharField(max_length=100,verbose_name=_('car class tilte'))
    description = models.TextField(blank=True, verbose_name=_('description'))
    image = models.ImageField(blank=True , upload_to='media/image', verbose_name=_('image'))

    def get_absolute_url(self):
        return reverse('pages:show_by_brand', args={self.pk})

    def __str__(self):
        return self.title


class CarBrand(models.Model):
    car_class = models.ForeignKey(CarClass, related_name='car_class', on_delete=models.CASCADE, verbose_name=_('car class'))
    title = models.CharField(max_length=20, verbose_name=_('car brand title'))
    description = models.TextField(verbose_name=_('description') , blank=True,)
    image = models.ImageField(blank=True , upload_to='media/image',verbose_name=_('image'))

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('pages:car_brand_subset', args={self.pk})


class Car(models.Model):
    car_brand = models.ForeignKey(CarBrand, related_name='car_brand', on_delete=models.CASCADE, verbose_name=_('car brand'))
    title = models.CharField(max_length=200,verbose_name=_('car title'))
    description = models.TextField(verbose_name=_('description'), blank=True)
    image = models.ImageField(blank=True , upload_to='media/image',verbose_name=_('image'))

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('pages:car_show',args={self.pk})


class Comment(models.Model):
    author = models.ForeignKey(get_user_model(),on_delete=models.CASCADE,verbose_name=_('autor'))
    car = models.ForeignKey(Car,on_delete=models.CASCADE, related_name='car',verbose_name=_('car'))
    text = models.TextField(max_length=400, verbose_name=_('comment text'))
    date_time_created = models.DateTimeField(verbose_name=_('date time created'),auto_now_add=True)
    date_time_modified = models.DateTimeField(verbose_name=_('date time modified'),auto_now=True,blank=True)

    def __str__(self):
        return self.text
