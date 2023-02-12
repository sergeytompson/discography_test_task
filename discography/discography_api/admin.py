from django.contrib import admin

from .models import Performer, Album, Song, AlbumSongs


@admin.register(Performer)
class PerformerAdmin(admin.ModelAdmin):
    list_display = ("pk", "name",)
    list_display_links = ("pk", "name",)
    search_fields = ("name",)


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ("pk", "name",)
    list_display_links = ("pk", "name",)
    search_fields = ("name",)
    list_filter = ("year_of_issue", "performer",)
    list_select_related = ("performer",)


@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ("pk", "name",)
    list_display_links = ("pk", "name",)
    search_fields = ("name",)


@admin.register(AlbumSongs)
class AlbumSongsAdmin(admin.ModelAdmin):
    list_display = ("pk", "album", "song", "serial_number",)
    list_display_links = ("pk",)
    search_fields = ("album", "song",)
    list_filter = ("album",)
    list_select_related = ("album", "song",)
