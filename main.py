from cryptocurrency import Cryptocurrency
from api import callCryptoAPI, callForexAPI
from config import *

# INITIALIZING GLOBALS
cryptoData = callCryptoAPI(cryptoAPIKey, ",".join(cryptoIDs));
forexData = callForexAPI(forexAPIKey);

purchasesFile = open('./investment-data/purchase-history', 'r');
purchasesData = purchasesFile.readlines();
purchasesFile.close();

cryptos = [];
for i in range(len(cryptoIDs)):
    cryptos.append(Cryptocurrency(cryptoIDs[i], cryptoSymbols[i]));

for crypto in cryptos:
    crypto.updateProperties(cryptoData, purchasesData);
    print(crypto.netProfit);


# HUFEUR = forexData["conversion_rates"]["HUF"];
# RONEUR = forexData["conversion_rates"]["RON"];
# USDEUR = forexData["conversion_rates"]["USD"];