from rich.theme import Theme;
from rich.console import Console;
from rich.table import Table;
from cryptocurrency import Cryptocurrency;
from api import callCryptoAPI, callForexAPI;
from utils import styleDecider;
from config import *;

# INITIALIZE TABLE
console = Console();
table = Table(title = "BOBCAT");
table.add_column("Coin"); table.add_column("Amount"); table.add_column("Cost"); table.add_column("Current Value"); table.add_column("Net Profit");

def fillTable(coin):
    currentStyle = styleDecider(coin.netProfit);
    table.add_row(coin.symbol, str(coin.amount), str(coin.cost), str(coin.currentValue), "[" + currentStyle + "]" + str(coin.netProfit) + "[/" + currentStyle + "]");

# INITIALIZING GLOBALS
with console.status("Loading...", spinner="dots"):
    cryptoData = callCryptoAPI(cryptoAPIKey, ",".join(cryptoIDs));
    forexData = callForexAPI(forexAPIKey);
    fiatQuotes = [forexData["conversion_rates"][fiat] for fiat in fiatCurrencies];

    purchasesFile = open('./investment-data/purchase-history', 'r');
    purchasesData = purchasesFile.readlines();
    purchasesFile.close();
    
    cryptos = [];
    for i in range(len(cryptoIDs)):
        cryptos.append(Cryptocurrency(cryptoIDs[i], cryptoSymbols[i]));
        cryptos[i].updateProperties(cryptoData, purchasesData);
        fillTable(cryptos[i]);
    total = Cryptocurrency('0', 'TOTAL');
    total.amount = '-'; total.cost = 0; total.currentValue = 0; total.netProfit = 0;
    for coin in cryptos:
        total.cost += coin.cost;
        total.currentValue += coin.currentValue;
        total.netProfit += coin.netProfit;
    fillTable(total);

# START
console.print(table);
