import requests; import json;
from config import cryptoAPIKey, forexAPIKey, cryptoIDs, baseCurrency, fiatCurrencies;
from os.path import exists, getmtime;
from datetime import datetime, timedelta;

def hasValidCache(fileName, hours):
    return exists(fileName) and datetime.now() - datetime.fromtimestamp(getmtime(fileName)) < timedelta(hours);

def callCryptoAPI():
    cryptoIDList = ",".join(cryptoIDs);
    params = { 'id': cryptoIDList, 'convert': baseCurrency };
    headers = { 'Accepts': 'application/json', 'X-CMC_PRO_API_KEY': cryptoAPIKey };
    request = requests.get("https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest", params=params, headers=headers);
    return request.json();

def callForexAPI():
    request = requests.get(f"https://v6.exchangerate-api.com/v6/{forexAPIKey}/latest/{baseCurrency}");
    return request.json();

def getCryptoData():
    if hasValidCache("./cache/coinmarketcap", 1):
        cache = open("./cache/coinmarketcap", "r");
        cryptoData = json.loads(cache.read());
        cache.close();
    else:
        cryptoData = callCryptoAPI();
        cache = open("./cache/coinmarketcap", "w");
        cache.write(json.dumps(cryptoData));
        cache.close();
    return cryptoData;

def getForexData():
    if hasValidCache("./cache/forex", 12):
        cache = open("./cache/forex", "r");
        forexData = json.loads(cache.read());
        cache.close();
    else:
        forexData = callForexAPI();
        cache = open("./cache/forex", "w");
        cache.write(json.dumps(forexData));
        cache.close();
    return [forexData["conversion_rates"][fiat] for fiat in fiatCurrencies];