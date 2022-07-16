import requests
import json

popular_currency = [
    "BTC",
    "ETH",
    "USDT",
    "USDC",
    "BNB",
    "BUSD",
    "XRP",
    "ADA",
    "SOL",
    "DOT"
]


def getCoipaprikaData():
    url = 'https://api.coinpaprika.com/v1/tickers'
    res = requests.get(url)
    data = res.json()
    data_filtered = {}
    for item in data:
        if(popular_currency.count(item['symbol'])>0):
            data_filtered[item['symbol']] =( '%.5f' % (item['quotes']['USD']['price']))
    return data_filtered


def getCoinstatData():
    url = 'https://api.coinstats.app/public/v1/coins?skip=0&limit=25&currency=USD'
    res = requests.get(url)
    data = res.json()
    # print(type(data))
    data_filtered = {}
    for item in data['coins']:
        if(popular_currency.count(item['symbol'])>0):
            data_filtered[item['symbol']] =( '%.5f' % (item['price']))
    return data_filtered


def getKucoinData():
    url = 'https://api.kucoin.com/api/v1/prices?base=USD'
    res = requests.get(url)
    data = res.json()
    data_filtered = {}
    for item in data['data']:
        if(popular_currency.count(item)>0):
            data_filtered[item] =( '%.5f' % float(data['data'][item]))
    return data_filtered


def getCoinbaseData():
    urlBase = 'https://api.coinbase.com/v2/exchange-rates?currency='
    data_filtered = {}
    urlArray = list(map(lambda x: urlBase + x, popular_currency))
    for obj in urlArray:
        res = requests.get(obj)
        data = res.json()
        data_filtered[data['data']['currency']] = ( '%.5f' % float(data['data']['rates']['USD']))
    print(data_filtered)


def getCoinmarketData():
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    res=requests.get(url, headers={'X-CMC_PRO_API_KEY': 'f4e05ef5-d516-4b8e-811c-58f82c177b11'})
    data = res.json()
    data_filtered = {}
    for item in data['data']:
        if(popular_currency.count(item['symbol'])>0):
            data_filtered[item['symbol']] =( '%.5f' % float(item['quote']['USD']['price']))
    return data_filtered


allowedMarkets = [getCoinmarketData, getCoinstatData, getKucoinData, getCoipaprikaData, getCoinbaseData, getCoinmarketData]