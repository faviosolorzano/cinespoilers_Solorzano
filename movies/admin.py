from django.contrib import admin
from .models import Movie, Genre


# NUEVO
@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']
    ordering = ['id']


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'release_year', 'director', 'is_active']
    list_filter = ['is_active', 'release_year']
    search_fields = ['title', 'director']
    ordering = ['id']
    filter_horizontal = ['genres']  # NUEVO: widget cómodo para ManyToMany