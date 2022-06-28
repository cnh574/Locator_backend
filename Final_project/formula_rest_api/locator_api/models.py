from django.db import models

# Cclass Contact(models.Model):

class Locator(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    image= models.CharField(max_length=300)

