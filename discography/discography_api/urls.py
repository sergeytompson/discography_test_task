from django.urls import include, path
from rest_framework import routers

from .views import AlbumDetailAPIView, PerformerViewSet

router = routers.SimpleRouter()
router.register(
    r"performer",
    PerformerViewSet,
    basename="performer",
)

urlpatterns = [
    path("", include(router.urls)),
    path(
        "performer/<int:performer_pk>/album/<int:album_pk>/",
        AlbumDetailAPIView.as_view(),
    ),
]
