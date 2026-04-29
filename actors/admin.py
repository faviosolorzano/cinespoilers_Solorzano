from django.contrib import admin
from .models import Actor


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'nationality']
    search_fields = ['first_name', 'last_name']
    ordering = ['id']
    filter_horizontal = ['movies']