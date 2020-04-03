from django.contrib import admin

from .models import Country, City


class CityInline(admin.StackedInline):
    model = City
    extra = 3


class CountryAdmin(admin.ModelAdmin):
    inlines = [CityInline]


admin.site.register(Country, CountryAdmin)


class CityAdmin(admin.ModelAdmin):
    list_display = ['city', 'country']


admin.site.register(City, CityAdmin)
