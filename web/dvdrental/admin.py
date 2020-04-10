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


class FilmActorInline(admin.StackedInline):
    model = FilmActor
    extra = 1


class ActorAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name']
    search_fields = ['first_name', 'last_name']


admin.site.register(Actor, ActorAdmin)


class FilmAdmin(admin.ModelAdmin):
    list_display = ['title', 'release_year', 'language', 'length', 'rating']
    list_filter = ['categories']
    inlines = [FilmActorInline]


admin.site.register(Film, FilmAdmin)


class ActorInfoAdmin(admin.ModelAdmin):
    list_display = ['actor_id', 'first_name', 'last_name', 'film_info']
    list_per_page = 25
    search_fields = ['first_name', 'last_name']

    # actor_info is a data base materialized view, disable add, change and delete permissions
    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(ActorInfo, ActorInfoAdmin)
