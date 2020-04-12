from django.contrib import admin

from .models import *


class CityInline(admin.StackedInline):
    model = City
    extra = 1


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ['country']
    ordering = ['country']
    search_fields = ['country']
    inlines = [CityInline]


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


class FilmCategoryInline(admin.StackedInline):
    model = FilmCategory
    extra = 1


@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    list_display = ['title', 'release_year', 'language', 'length', 'rating']
    search_fields = ['title']
    list_filter = ['categories', 'language']

    fieldsets = (
        (None, {
            'fields': ('title', 'description', 'release_year', 'language', 'length', 'special_features', 'fulltext',
                       'rating')
        }),
        ('Rental', {
            'fields': ('rental_duration', 'rental_rate', 'replacement_cost')
        })
    )
    inlines = [FilmActorInline, FilmCategoryInline]
