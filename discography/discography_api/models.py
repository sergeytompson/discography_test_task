from django.db import models


class Performer(models.Model):
    name = models.CharField(
        "Исполнитель",
        max_length=150,
    )

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "Исполнитель"
        verbose_name_plural = "Исполнители"


class Album(models.Model):
    name = models.CharField(
        "Название альбома",
        max_length=150,
    )
    year_of_issue = models.IntegerField(
        "Год выпуска альбома",
    )
    performer = models.ForeignKey(
        Performer,
        on_delete=models.CASCADE,
        verbose_name="Исполнитель",
        related_name="albums",
    )

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "Альбом"
        verbose_name_plural = "Альбомы"


class Song(models.Model):
    name = models.CharField(
        "Песня",
        max_length=150,
    )

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "Песня"
        verbose_name_plural = "Песни"


class AlbumSongs(models.Model):
    album = models.ForeignKey(
        Album,
        on_delete=models.CASCADE,
        verbose_name="Альбом",
        related_name="songs",
    )
    song = models.ForeignKey(
        Song,
        on_delete=models.CASCADE,
        verbose_name="Песня",
    )
    serial_number = models.IntegerField(
        "Порядковый номер песни в альбоме",
    )

    class Meta:
        verbose_name = "Песня в альбоме"
        verbose_name_plural = "Песни в альбоме"
