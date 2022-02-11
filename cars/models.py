from django.db import models


# Create your models here.
class Specs(models.Model):
    name = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    weight = models.PositiveIntegerField()
