from typing import TypeVar, Type

from rest_framework import serializers
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.generics import RetrieveAPIView

from .serializers import (PerformerSerializer,
                          PerformerDetailSerializer,
                          AlbumDetailSerializer,)
from .models import Performer, Album

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
