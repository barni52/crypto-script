from config import baseCurrency;

class Cryptocurrency:
    def __init__(self, id, symbol):
        self.id = id;
        self.symbol = symbol;
        self.amount = self.cost = self.currentValue = self.netProfit = self.netProfitPercent = 0;

    def sumPurchases(self, purchasesData):
        for line in purchasesData:
            line = line.split();
            if line[1] == self.symbol:
                self.amount += float(line[2]);
                self.cost += float(line[3]);

    def updateData(self, cryptoData):
        self.name = cryptoData["data"][self.id]["name"];
        self.price = cryptoData["data"][self.id]["quote"][baseCurrency]["price"];
        self.fluctuations = [
            cryptoData["data"][self.id]["quote"][baseCurrency]["percent_change_24h"],
            cryptoData["data"][self.id]["quote"][baseCurrency]["percent_change_7d"],
            cryptoData["data"][self.id]["quote"][baseCurrency]["percent_change_30d"]
        ];

    def updateProperties(self, cryptoData, purchasesData):
        self.sumPurchases(purchasesData);
        self.updateData(cryptoData, baseCurrency);
        self.currentValue = self.amount * self.price;
        self.netProfit = self.currentValue - self.cost;
        self.netProfitPercent = self.netProfit / self.cost * 100;