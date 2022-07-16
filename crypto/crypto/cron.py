from currency.utils.coinMarkets import *
from currency.utils.avg import getAverageCurrencyRate
import requests

def my_scheduled_job():
    url = 'http://[your_host]:[your_port]/api/v1/currency/'
    header = {"Authorization": "Token 'YOUR_TOKEN'"}
    data = []
    avg = []
    for i in range(5):
        data[i] = allowedMarkets[i]()
    avg = getAverageCurrencyRate(data)
    requests.post(url, headers=header, json = avg)