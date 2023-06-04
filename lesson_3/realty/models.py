from django.db import models

class Realty(models.Model):
    name = models.CharField(max_length=50)
    adres = models.CharField(max_length=300)
    info = models.TextField()
    img_link = models.TextField()
    cat = models.ForeignKey('Category', null=True, blank=True, on_delete=models.PROTECT)

class Category(models.Model):
    cat = models.CharField(max_length=50)

    def __str__(self):
        return self.cat