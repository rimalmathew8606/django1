from django.db import models

class Movie(models.Model):
    movie=models.CharField(max_length=20)
    desc=models.TextField()
    year=models.IntegerField()
    image=models.ImageField(upload_to="Movies",null=True,blank=True)

    def __str__(self):
        return self.movie
