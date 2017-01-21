import pandas
import json
from Risky import *
from Money import *
class Strategy:
    _total_avg = {}
    _counter = 0
    _PERCENTAGE = .005
    _AMOUNTDAYS = 10
    risky = Risky()
    money = Money(0)
    def __init__(self, amount):
        self.money = Money(amount) #parameter is the amount of money to start with
    def mean_strategy(self,datum):
        """Uses mean reversion to decide if to buy, sell, or do nothing.
        Datum is what is returned by a yahoo finance api call on stocks. """
        decision = {}
        self._counter +=1
        for stock in datum["query"]["results"]["quote"]:
            stock_price = stock["Ask"]
            stock_name = stock["symbol"]

            self._total_avg[stock_name] = self.getAverage(self._AMOUNTDAYS,stock_name)
            stock_amount = 1 #for testing purposes buy/sell only one for now
            buy_range = self._PERCENTAGE*self._total_avg[stock_name]
	    try:
                stock_price = float(stock_price)
	    except TypeError:
		stock_price = self._total_avg[stock_name]
            if stock_price > buy_range+self._total_avg[stock_name]:
                if self.risky.risk(stock_name,stock_amount,2):
                    decision[stock_name]=[2, stock_amount]  #0 is nothing, 1 is buy, 2 is sell
                    self.money.add(stock_price)
                    self.risky.stock_counts[stock_name]-=1
                else:
                    decision[stock_name]= [0,0]

            elif stock_price < -1*buy_range+self._total_avg[stock_name]:
                if self.risky.risk(stock_name,stock_amount,1) and self.money.getMoney() > stock_price:
                    decision[stock_name]= [1, stock_amount]  #0 is nothing, 1 is buy, 2 is sell
                    self.money.remove(stock_price)
                    self.risky.stock_counts[stock_name]+=1

                else:
                    decision[stock_name] = [0,0]
            else:
                decision[stock_name] =  [0,0]
        self.writeToFile(decision,"Decisions.json","a")
        return decision


    def getAverage(self,amountDays,stock):
        """Gets the average close value of the stock over the last amountDays"""
        totals = 0
        days = 0
        total = 0
        with open("./ClosingData/"+stock+"Data.csv") as data:
            days = pandas.read_csv(data)
        length = len(days["Close"].values)
        for x in xrange(length-1,length-amountDays-1,-1):
            total+=days["Close"][x]
        totals = total/float(amountDays)
        return  totals

    def writeToFile(self,decision,filename,wa): #wa is if you want to write or append
        decision["Money"] = float(int(self.money.getMoney()*100))/100
        with open(filename,wa) as fp:
            json.dump(decision,fp)
            fp.write("\n")

    def sellAll(self,datum):
        for stock in datum["query"]["results"]["quote"]:
            stock_price = stock["Ask"]
            stock_name = stock["symbol"]
            stock_price = float(stock_price)
            while self.risky.risk(stock_name,1,2):
                self.money.add(stock_price)
                self.risky.stock_counts[stock_name]-=1
    def printDatMoney(self):
        return self.money.getMoney()



