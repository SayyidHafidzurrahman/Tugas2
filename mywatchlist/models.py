from django.db import models

class MyWatchListItem(models.Model):
    watched_movie = models.BooleanField()
    movie_name = models.CharField(max_length=255)
    movie_rating = models.IntegerField()
    release_date = models.DateField()
    movie_review = models.CharField(max_length=255)
# Create your models here.
