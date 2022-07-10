from cryptocurrency import Cryptocurrency
from api import callCryptoAPI, callForexAPI
from config import *

cryptoIDs = ['1', '328', '1027']

cryptoData = callCryptoAPI(cryptoAPIKey, ",".join(cryptoIDs));
forexData = callForexAPI(forexAPIKey);
print(forexData)

purchasesFile = open('./investment-data/purchase-history', 'r');
purchasesData = purchasesFile.readlines();
purchasesFile.close();

bitcoin = Cryptocurrency("1", "BTC")
bitcoin.updateProperties(cryptoData, purchasesData)
print(bitcoin.netProfit);

# cryptocurrencies = [ Cryptocurrency(id) for id in cryptoIDs ]

def display(coin):
    coin.updateProperties(cryptoData, purchasesData);


# HUFEUR = forexData["conversion_rates"]["HUF"];
# RONEUR = forexData["conversion_rates"]["RON"];
# USDEUR = forexData["conversion_rates"]["USD"];

# displayQuotes(cryptoIDs[1])