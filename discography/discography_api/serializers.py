from rest_framework import serializers

from .models import Performer, Album, AlbumSongs


class AlbumSongsSerializer(serializers.ModelSerializer):
    song = serializers.SlugRelatedField(slug_field="name", read_only=True,)

    class Meta:
        model = AlbumSongs
        fields = ("serial_number", "song",)


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ("pk", "name", "year_of_issue")


class AlbumDetailSerializer(serializers.ModelSerializer):
    songs = AlbumSongsSerializer(many=True, read_only=True,)

    class Meta:
        model = Album
        fields = ("pk", "name", "year_of_issue", "songs")


class PerformerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Performer
        fields = ("pk", "name",)


class PerformerDetailSerializer(serializers.ModelSerializer):
    albums = AlbumSerializer(many=True, read_only=True,)

    class Meta:
        model = Performer
        fields = ("pk", "name", "albums")
