from django.db import models

class Movie(models.Model):
    Title= models.CharField(max_length=120)
    Genre= models.CharField(max_length=50)
    Plot= models.CharField(max_length=255)
    Director=models.CharField(max_length=50)
    Actor=models.CharField(max_length=100)
    Year= models.IntegerField()
    Rating=models.IntegerField()
     
    def __str__(self):
            return self.Title  