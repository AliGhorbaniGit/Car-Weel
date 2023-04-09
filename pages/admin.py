from django.contrib import admin

from .models import CarClass,CarBrand,Car


class ChangeAdmin(admin.ModelAdmin):
    pass


admin.site.register(CarClass, ChangeAdmin)
admin.site.register(CarBrand, ChangeAdmin)
admin.site.register(Car, ChangeAdmin)