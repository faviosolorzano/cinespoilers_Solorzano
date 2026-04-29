from rest_framework import serializers
from .models import Movie, Genre


# NUEVO
class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = ['id', 'name']
        read_only_fields = ['id']


class MovieSerializer(serializers.ModelSerializer):
    # CAMBIO: genres anidado como lista de objetos
    genres = GenreSerializer(many=True, read_only=True)
    # NUEVO: para escribir géneros al crear/editar una película
    genre_ids = serializers.PrimaryKeyRelatedField(
        many=True,
        write_only=True,
        queryset=Genre.objects.all(),
        source='genres'
    )

    class Meta:
        model = Movie
        fields = [
            'id',
            'title',
            'synopsis',
            'release_year',
            'director',
            'duration_minutes',
            'is_active',
            'genres',      # lectura: objetos completos
            'genre_ids',   # escritura: lista de ids
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']