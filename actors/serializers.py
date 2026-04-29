from rest_framework import serializers
from .models import Actor


class ActorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Actor
        fields = [
            'id',
            'first_name',
            'last_name',
            'birth_date',
            'nationality',
            'bio',
            'movies',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']