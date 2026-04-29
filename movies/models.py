from django.db import models


# NUEVO
class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ['id']
        verbose_name = 'Género'
        verbose_name_plural = 'Géneros'

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=255)
    synopsis = models.TextField(blank=True, default='')
    release_year = models.PositiveIntegerField()
    director = models.CharField(max_length=255, blank=True, default='')
    duration_minutes = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    genres = models.ManyToManyField(Genre, blank=True)  # NUEVO
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['id']
        verbose_name = 'Película'
        verbose_name_plural = 'Películas'

    def __str__(self):
        return f"{self.title} ({self.release_year})"