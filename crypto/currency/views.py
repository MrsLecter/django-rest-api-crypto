from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from .models import CurrencyRate
from .serializers import CurrencySerializer
from .utils.coinMarkets import *
import json
from rest_framework.permissions import IsAuthenticated


class CurrencyViewSet(viewsets.ModelViewSet):
    queryset = CurrencyRate.objects.all()
    serializer_class = CurrencySerializer
    permission_classes = [IsAuthenticated]

# class CurrencyView(APIView):
#     def get(self, request):
#         data = CurrencyRate.objects.all().values()

#         return Response({'data': CurrencySerializer(data, many=True).data})


#     def post(self, request):
#         # input error prevention
#         serialize = CurrencySerializer(data = request.data)
#         serialize.is_valid(raise_exception = True)
#         # if data is valid
#         # calls the method create() from serializers.py
#         serialize.save()

#         return Response({'post': serialize.data})

#     def delete(self, request, *args, **kwargs):
#         id = kwargs.get("id", None)
#         if not id :
#             return Response({'error': "Current [id] not found!"})

#         try:
#             instance = CurrencyRate.objects.get(id = id)
#         except:
#             return Response({'error': "Current [id] not found!"})


#         serializer = CurrencySerializer(data=request.data, instance = instance)
#         serializer.is_valid()
#         serializer.delete(id)

#         return Response({'delete': f'delete note with id={id}'})

class MarketView(APIView):
    def get(self, request, *args, **kwargs):
        allowedMarkets = {'coinmarket': getCoinmarketData, "coinstats": getCoinstatData, "kucoin": getKucoinData, "coinpaprika": getCoipaprikaData, "coinbase": getCoinbaseData, "coinmarket": getCoinmarketData}
        market = kwargs.get("market", None)
        # check if market available
        if(allowedMarkets.get(market)== None):
            return Response({'error': f'coinmarket [{market}] not found'})
        else: 
            data = allowedMarkets[market]()
            return Response({'data': data})

       
