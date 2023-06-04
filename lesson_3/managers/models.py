from django.db import models

class Managers(models.Model):
    name = models.CharField(max_length=50)
    telefon = models.CharField(max_length=300)
    email = models.TextField()

