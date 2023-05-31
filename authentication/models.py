from django.db import models

class Movie(models.Model):
    Title= models.CharField(max_length=120)
    Genre= models.CharField(max_length=50)
    Plot= models.CharField(max_length=255)
    Director=models.CharField(max_length=50)
    Actor=models.CharField(max_length=100)
    Year= models.IntegerField()
    Rating=models.IntegerField()
    class Meta:
          app_label="authentication"
    def __str__(self):
            return f"{self.Title} - {self.Plot} - {self.Genre} - {self.Director} - {self.Rating} - {self.Year}" 