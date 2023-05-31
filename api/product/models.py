from django.db import models

class Product(models.Model):

    name = models.CharField(max_length=255)
    price = models.FloatField()
    description = models.CharField(max_length=2000)
    image_url = models.CharField(max_length=2000)

    def __str__(self):
        return self.name