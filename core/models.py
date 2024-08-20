from django.db import models

class EthereumPriceFeed(models.Model):
    roundId = models.CharField(max_length=255, unique=True)
    priceUSD = models.CharField(max_length=255)
    timestamp = models.IntegerField(help_text='Unix timestamp')