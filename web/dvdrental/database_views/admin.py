from django.contrib import admin

from .models import *


class MaterializedViewModelAdmin(admin.ModelAdmin):
    # Disable add, change and delete permissions for data base materialized views
    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(ActorInfo)
class ActorInfoAdmin(MaterializedViewModelAdmin):
    list_display = ['actor_id', 'first_name', 'last_name', 'film_info']
    list_per_page = 25
    search_fields = ['first_name', 'last_name']


@admin.register(CustomerList)
class CustomerListAdmin(MaterializedViewModelAdmin):
    list_display = [x.name for x in CustomerList._meta.fields]
    search_fields = ['name', 'address', 'city', 'country']
