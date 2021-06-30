from django.db import models


# Create your models here.
class Party(models.Model):
    name = models.CharField(max_length=32)
    name_abbr = models.CharField(max_length=8)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='생성 시간')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='수정 시간')

    class Meta:
        db_table = 'parties'


class Artist(models.Model):
    name = models.CharField(max_length=32)
    name_abbr = models.CharField(max_length=8)
    parties = models.ManyToManyField(Party, through='ArtistParty')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='생성 시간')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='수정 시간')

    class Meta:
        db_table = 'artists'


class ArtistParty(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, null=True)
    party = models.ForeignKey(Party, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = 'artists_parties'
