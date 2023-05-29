from django.db import models

# Create your models here.
class Food(models.Model):
    name = models.CharField(max_length=50)
    intro = models.CharField(max_length=300)
    info = models.TextField()
    img_link = models.TextField()