from django.db import models

# Create your models here.


class Spot(models.Model):
    title = models.CharField(max_length=64)
    location=models.CharField(max_length=64)
    description=models.CharField(max_length=1024)
    image=models.CharField(max_length=64)
    creator=models.CharField(max_length=64)
    def __str__(self):
        return f"Spot:{self.id} at {self.title}"

class Message(models.Model):
    content = models.CharField(max_length=1024)
    date=models.CharField(max_length=64)
    creator=models.CharField(max_length=64)
    spot= models.IntegerField()
    def __str__(self):
        return f"{self.creator} wrote:{self.id} Message"

