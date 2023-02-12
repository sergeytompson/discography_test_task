from django.urls import path, include
from rest_framework import routers

from .views import PerformerViewSet, AlbumDetailAPIView


router = routers.SimpleRouter()
router.register(r"performer", PerformerViewSet, basename="performer",)

urlpatterns = [
    path("", include(router.urls)),
    path("performer/<int:pk>/album/<int:pk2>/", AlbumDetailAPIView.as_view(),)
]
