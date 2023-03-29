from django.contrib import admin

from .models import CarClass


class ChangeAdmin(admin.ModelAdmin):
    pass


admin.site.register(CarClass, ChangeAdmin)

