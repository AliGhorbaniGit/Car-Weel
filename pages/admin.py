from django.contrib import admin

from .models import CarClass,CarClassSUb


class ChangeAdmin(admin.ModelAdmin):
    pass


admin.site.register(CarClass, ChangeAdmin)
admin.site.register(CarClassSUb, ChangeAdmin)
