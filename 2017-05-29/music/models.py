from django.db import models

# Create your models here.
class Album(models.Model):
    """docstring for Album"""
    album_artist = models.CharField(max_length = 255)
    album_title = models.CharField(max_length = 550)
    album_genre = models.CharField(max_length = 100)
    album_logo = models.CharField(max_length = 255)
    def __str__(self):
        return self.album_artist + ' - ' + self.album_title

class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    file_type =  models.CharField(max_length = 10)
    file_name =  models.CharField(max_length = 100)
    is_favorite = models.BooleanField(default = False)
    def __str__(self):
        return self.file_name
