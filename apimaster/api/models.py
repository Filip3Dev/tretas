from django.db import models
from decimal import Decimal

class Coinlist(models.Model):
    SHIRT_SIZES = (
        ('T', 'True'),
        ('F', 'False')
    )
    """This class represents the bucketlist model."""
    name = models.CharField(max_length=255, blank=False)
    nick = models.CharField(max_length=10, blank=False)
    ammount = models.IntegerField(blank=False)
    worth = models.DecimalField(max_digits=24, decimal_places=8,default=Decimal('0.00000000'))
    roi = models.IntegerField(blank=False)
    logo = models.CharField(max_length=500, blank=False)
    nodecount = models.IntegerField()
    coinslocked = models.IntegerField()
    sharetime = models.TimeField()
    active = models.CharField(max_length=1, choices=SHIRT_SIZES)
    price = models.DecimalField(max_digits=24, decimal_places=8,default=Decimal('0.00000000'))
    mcap = models.CharField(max_length=255)
    weekcoins = models.DecimalField(max_digits=10, decimal_places=5)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nick
# Create your models here.
