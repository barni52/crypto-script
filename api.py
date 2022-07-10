import requests;

def callCryptoAPI(key, cryptoIDs = '1', baseCurrency = "EUR"):
    params = { 'id': cryptoIDs, 'convert': baseCurrency };
    headers = { 'Accepts': 'application/json', 'X-CMC_PRO_API_KEY': key };
    request = requests.get("https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest", params=params, headers=headers);
    return request.json();

def callForexAPI(key, baseCurrency = "EUR"):
    request = requests.get("https://v6.exchangerate-api.com/v6/" + key + "/latest/" + baseCurrency);
    return request.json();