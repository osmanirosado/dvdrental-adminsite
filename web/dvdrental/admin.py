from django.contrib import admin

from .models import *


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ['name']
    ordering = ['name']
    search_fields = ['name']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    ordering = ['name']
    search_fields = ['name']


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name']
    list_display_links = ['first_name', 'last_name']
    ordering = ['last_name', 'first_name']
    search_fields = ['first_name', 'last_name']


class FilmCategoryInline(admin.StackedInline):
    model = FilmCategory
    autocomplete_fields = ['category']
    extra = 1


class FilmActorInline(admin.StackedInline):
    model = FilmActor
    autocomplete_fields = ['actor', 'film']
    extra = 1


@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    list_display = ['title', 'release_year', 'language', 'length', 'rating']
    ordering = ['release_year', 'title']
    search_fields = ['title']
    list_filter = ['categories', 'language']

    fieldsets = (
        ('Film Details', {
            'fields': ('title', 'description', 'release_year', 'language', 'length', 'rating')
        }),
        ('More Film Details', {
            'fields': ('special_features', 'fulltext')
        }),
        ('Rental Conditions', {
            'fields': ('rental_duration', 'rental_rate', 'replacement_cost')
        })
    )
    inlines = [FilmActorInline, FilmCategoryInline]


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ['city', 'country']
    ordering = ['country', 'city']
    search_fields = ['city']
    autocomplete_fields = ['country']


class CityInline(admin.StackedInline):
    model = City
    extra = 1


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ['country']
    ordering = ['country']
    search_fields = ['country']
    inlines = [CityInline]


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ['address', 'address2', 'district', 'city']
    ordering = ['city', 'district', 'address']
    search_fields = ['address', 'address2', 'district', 'city__city']
    autocomplete_fields = ['city']


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'create_date', 'store_id']
    list_display_links = ['first_name', 'last_name']
    ordering = ['last_name', 'first_name']
    search_fields = ['first_name', 'last_name', 'email']
    autocomplete_fields = ['address']


@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'active']
    list_display_links = ['first_name', 'last_name']
    ordering = ['last_name', 'first_name']
    search_fields = ['first_name', 'last_name', 'email']
    autocomplete_fields = ['address']


@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    list_display = ['inventory_id', 'film', 'store_id']
    ordering = ['store_id', 'film']
    search_fields = ['film__title']
    autocomplete_fields = ['film']
