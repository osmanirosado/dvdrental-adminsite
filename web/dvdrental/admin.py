from django.contrib import admin

from .models import Country, City

admin.site.register(Country)


class CityAdmin(admin.ModelAdmin):
    list_display = ['city', 'country']


admin.site.register(City, CityAdmin)
