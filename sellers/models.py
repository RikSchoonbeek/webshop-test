from django.db import models


class Seller(models.Model):
    username = models.CharField(max_length=30)
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    birthday = models.DateField()

    def __str__(self):
        return self.username
