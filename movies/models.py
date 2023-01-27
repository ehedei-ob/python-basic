from django.db import models


class Director(models.Model):
    full_name = models.CharField(max_length=100)
    birthdate = models.DateField()
    biography = models.TextField(null=True)

    def __str__(self):
        return self.full_name


class Movie(models.Model):
    director = models.ForeignKey('Director', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    sinopsis = models.TextField(null=True)
    year = models.PositiveIntegerField()

    def __str__(self):
        return self.title

