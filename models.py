from django.db import models

class Stuf(models.Model):
    name = models.CharField(max_length=222)
    description = models.TextField()
    price = models.FloatField()
    stock = models.IntegerField()
