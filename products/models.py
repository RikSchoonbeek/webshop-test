from django.db import models

from sellers.models import Seller


class Product(models.Model):
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    description = models.TextField()
    price = models.FloatField()
    stock = models.IntegerField()
    seller = models.ForeignKey(Seller)

    def __str__(self):
        return self.name
