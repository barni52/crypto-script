import requests

cryptoAPIkey = 'f9474327-4c7f-4712-ac0e-b4892c295a3f';

cryptocurrency = ['BTC', 'XMR', 'ETH'];
cryptoIDs = ['1', '328', '1027'];

# params = { 'id': ",".join(cryptoIDs) };
# headers = { 'Accepts': 'application/json', 'X-CMC_PRO_API_KEY': cryptoAPIkey };
# cryptoRequest = requests.get("https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest", params=params, headers=headers);
# cryptoData = cryptoRequest.json();

# def displayQuotes(cryptoID):
#     crypto = cryptoData["data"][cryptoID]["quote"]["USD"];
#     print("Current Market Price: " + str(crypto["price"]));

purchasesFile = open('./investment-data/purchase-history', 'r');
purchasesData = purchasesFile.readlines();
purchasesFile.close();

def processPurchaseData(coin):
    totalAmount = 0; boughtFor = 0;
    for line in purchasesData:
        line = line.split();
        if line[1] == coin:
            totalAmount += float(line[2]);
            boughtFor += float(line[3]);
    print(totalAmount)



# BTC = cryptoData["data"]["1"]["quote"]["EUR"];
# BTC_Price = BTC["price"];
# BTC_Change24h = BTC["percent_change_24h"];
# BTC_Change7d = BTC["percent_change_7d"];
# BTC_Change30d = BTC["percent_change_30d"];

# XMR = cryptoData["data"]["328"]["quote"]["EUR"];
# XMR_Price = XMR["price"];
# XMR_Change24h = XMR["percent_change_24h"];
# XMR_Change7d = XMR["percent_change_7d"];
# XMR_Change30d = XMR["percent_change_30d"];

# ETH = cryptoData["data"]["1027"]["quote"]["EUR"];
# ETH_Price = ETH["price"];
# ETH_Change24h = ETH["percent_change_24h"];
# ETH_Change7d = ETH["percent_change_7d"];
# ETH_Change30d = ETH["percent_change_30d"];


# forexKey = '14ee205d58124df32a9bd7e5';
# forexRequest = requests.get("https://v6.exchangerate-api.com/v6/" + forexKey + "/latest/EUR");
# forexData = forexRequest.json();

# HUFEUR = forexData["conversion_rates"]["HUF"];
# RONEUR = forexData["conversion_rates"]["RON"];
# USDEUR = forexData["conversion_rates"]["USD"];



# displayQuotes(cryptoIDs[1])