from dataclasses import fields
from .models import CurrencyRate
from django.http import JsonResponse
from rest_framework import serializers



# all fields are required
class CurrencySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only = True)
    BTC = serializers.CharField(max_length=7)
    ETH = serializers.CharField(max_length=7)
    USDT = serializers.CharField(max_length=7)
    USDC = serializers.CharField(max_length=7)
    BNB = serializers.CharField(max_length=7)
    BUSD = serializers.CharField(max_length=7)
    XRP = serializers.CharField(max_length=7)
    ADA = serializers.CharField(max_length=7)
    SOL = serializers.CharField(max_length=7)
    DOT = serializers.CharField(max_length=7)
    timestamp = serializers.DateTimeField(read_only = True)

    def create(self, validatedData):
        # unpacks the dictionary validatedData
        return CurrencyRate.objects.create(**validatedData)

    def delete(self, id):
        return CurrencyRate.objects.filter(id=id).delete()

# class CurrencySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CurrencyRate
#         fields = "__all__"