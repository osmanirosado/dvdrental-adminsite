from django.contrib import admin

from .models import *


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
