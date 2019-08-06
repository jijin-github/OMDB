from django.db import models

class Actor(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class MovieDetails(models.Model):
    title = models.CharField(max_length=50)
    rated = models.CharField(max_length=30)
    imdbID = models.CharField(unique=True, max_length=30)
    actors = models.ManyToManyField(Actor, blank=True, null=True, related_name='actors')

    def __str__(self):
        return self.title