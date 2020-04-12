from django.contrib import admin

from .models import *


class CityInline(admin.StackedInline):
    model = City
    extra = 3


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    inlines = [CityInline]
    search_fields = ['country']


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ['city', 'country']
    ordering = ['country', 'city']
    search_fields = ['city']


class FilmActorInline(admin.StackedInline):
    model = FilmActor
    extra = 1


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name']
    ordering = ['last_name', 'first_name']
    search_fields = ['first_name', 'last_name']


@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    list_display = ['title', 'release_year', 'language', 'length', 'rating']
    list_filter = ['categories']
    inlines = [FilmActorInline]
