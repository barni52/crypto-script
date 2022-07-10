from rich.theme import Theme;
from rich.console import Console;
from rich.table import Table;
from rich import box;
from cryptocurrency import Cryptocurrency;
from api import callCryptoAPI, callForexAPI;
from utils import *;
from config import *;
import json

def fillTable(coin):
    currentStyle = styleDecider(coin.netProfit);
    table.add_row(coin.symbol, str(coin.amount), f"€{str(coin.cost)}", f"{toHUF(coin.cost)}HUF", f"{toRON(coin.cost)}RON", "€" + str(round(coin.currentValue, 2)),
    f"€[{currentStyle}]{str(round(coin.netProfit, 2))}[/{currentStyle}]", f"[{currentStyle}]{str(round(coin.netProfitPercent, 2))}%[/{currentStyle}]");

console = Console();
with console.status("Loading...", spinner="dots"):
    if olderThan("./cache/cryptoDataCache", 1):
        cryptoData = callCryptoAPI(cryptoAPIKey, ",".join(cryptoIDs));
        cryptoDataCache = open("./cache/cryptoDataCache", "w");
        cryptoDataCache.write(json.dumps(cryptoData));
        cryptoDataCache.close();
    else:
        cryptoDataCache = open("./cache/cryptoDataCache", "r");
        cryptoData = json.loads(cryptoDataCache.read());
        cryptoDataCache.close();

    forexData = callForexAPI(forexAPIKey);
    fiatQuotes = [forexData["conversion_rates"][fiat] for fiat in fiatCurrencies];

    table = Table(caption = f'Last updated {cryptoData["status"]["timestamp"]}', box = box.SIMPLE, show_lines = True, highlight = True, padding = (0, 1));
    table.add_column("Coin"); table.add_column("Amount"); table.add_column("Cost"); table.add_column(""); table.add_column(""); table.add_column("Current Value"); table.add_column("Net Profit"); table.add_column("% Change");
    
    purchasesFile = open('./investment-data/purchase-history', 'r');
    purchasesData = purchasesFile.read();
    purchasesFile.close();
    
    cryptos = [];
    for i in range(len(cryptoIDs)):
        cryptos.append(Cryptocurrency(cryptoIDs[i], cryptoSymbols[i]));
        cryptos[i].updateProperties(cryptoData, purchasesData);
        fillTable(cryptos[i]);
    
    # TOTAL DATA
    total = Cryptocurrency('0', 'TOTAL');
    total.amount = '-'; total.cost = 0; total.currentValue = 0; total.netProfit = 0;
    for coin in cryptos:
        total.cost += coin.cost;
        total.currentValue += coin.currentValue;
        total.netProfit += coin.netProfit;
    total.netProfitPercent = total.netProfit / total.cost * 100;
    
    fillTable(total);

# DISPLAY DATA
console.print(table);