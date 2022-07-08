import requests

# BTC, XMR, ETH
cryptoAPIkey = 'f9474327-4c7f-4712-ac0e-b4892c295a3f';
cryptoIDs = ['1', '328', '1027'];

params = { 'id': ",".join(cryptoIDs), 'convert': 'EUR' };
headers = { 'Accepts': 'application/json', 'X-CMC_PRO_API_KEY': cryptoAPIkey };
response = requests.get("https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest", params=params, headers=headers)

print(response.json())

forexKey = '14ee205d58124df32a9bd7e5';
forexRequest = requests.get("https://v6.exchangerate-api.com/v6/" + forexKey + "/latest/EUR");
forexData = forexRequest.json();
