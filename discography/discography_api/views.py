from typing import Type, TypeVar

from rest_framework import serializers
from rest_framework.generics import RetrieveAPIView
from rest_framework.viewsets import ReadOnlyModelViewSet

from .models import Album, Performer
from .serializers import (AlbumDetailSerializer, PerformerDetailSerializer,
                          PerformerSerializer)

T = TypeVar("T", bound=serializers.ModelSerializer)


class PerformerViewSet(ReadOnlyModelViewSet):
    serializer_class = PerformerSerializer
    queryset = Performer.objects.all()

    def get_serializer_class(self) -> Type[T]:
        if self.action == "retrieve":
            return PerformerDetailSerializer
        return super().get_serializer_class()


class AlbumDetailAPIView(RetrieveAPIView):
    serializer_class = AlbumDetailSerializer
    lookup_url_kwarg = "pk2"

    def get_queryset(self):
        return Album.objects.filter(performer=self.kwargs["pk"])
