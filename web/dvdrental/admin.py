from django.contrib import admin

from .models import *


class CityInline(admin.StackedInline):
    model = City
    extra = 3


class CountryAdmin(admin.ModelAdmin):
    inlines = [CityInline]
    search_fields = ['country']


admin.site.register(Country, CountryAdmin)


class CityAdmin(admin.ModelAdmin):
    list_display = ['city', 'country']
    search_fields = ['city']


admin.site.register(City, CityAdmin)


class FilmAdmin(admin.ModelAdmin):
    list_display = ['title', 'release_year', 'language', 'length', 'rating']
    list_filter = ['categories']


admin.site.register(Film, FilmAdmin)
