from django.db import models

class Movie(models.Model):
  title = models.CharField(max_length=255)
  poster = models.URLField()
  genre = models.CharField(max_length=255)
  rating = models.FloatField(blank=True, null=True)
  year_release = models.IntegerField()
  metacritic_rating = models.IntegerField(blank=True, null=True)
  runtime = models.IntegerField()

  def __str__(self):
    return self.title
