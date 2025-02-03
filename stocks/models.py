from django.db import models

class Stock(models.Model):

    ticker = models.CharField(max_length=10)
    price = models.FloatField()
    change = models.FloatField()
