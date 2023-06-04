from django.db import models

class Request(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=300)
    question = models.TextField()
