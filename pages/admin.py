from django.contrib import admin

from .models import CarClass,CarBrand,Car,Comment


class ChangeAdmin(admin.ModelAdmin):

admin.site.register(Car, ChangeAdmin)
admin.site.register(CarClass, ChangeAdmin)
admin.site.register(CarBrand, ChangeAdmin)
admin.site.register(Comment, ChangeAdmin)
