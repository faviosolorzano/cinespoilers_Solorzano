from django.db import models
from movies.models import Movie


class Actor(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birth_date = models.DateField(blank=True, null=True)
    nationality = models.CharField(max_length=100, blank=True, default='')
    bio = models.TextField(blank=True, default='')
    movies = models.ManyToManyField(Movie, blank=True, related_name='actors')  # NUEVO
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['id']
        verbose_name = 'Actor'
        verbose_name_plural = 'Actores'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"