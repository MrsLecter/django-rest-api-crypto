from uuid import uuid4
from django.db import models 
import uuid

class CurrencyRate(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    BTC = models.CharField(max_length=7)
    ETH = models.CharField(max_length=7)
    USDT = models.CharField(max_length=7)
    USDC = models.CharField(max_length=7)
    BNB = models.CharField(max_length=7)
    BUSD = models.CharField(max_length=7)
    XRP = models.CharField(max_length=7)
    ADA = models.CharField(max_length=7)
    SOL = models.CharField(max_length=7)
    DOT = models.CharField(max_length=7)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.id
