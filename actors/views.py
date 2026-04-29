from rest_framework import viewsets
from .models import Actor
from .serializers import ActorSerializer


class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.prefetch_related('movies').all()
    serializer_class = ActorSerializer