import pandas
class Strategy:
    _total_avg = {}
    _counter = 0
    _PERCENTAGE = .10
    _AMOUNTDAYS = 10
    def mean_strategy(self,datum):
        """Uses mean reversion to decide if to buy, sell, or do nothing.
        Datum is what is returned by a yahoo finance api call on stocks. """
        decision = []
        self._counter +=1
        for stock in datum["query"]["results"]["quote"]:
            stock_price = stock["Ask"]
            stock_name = stock["symbol"]

            self._total_avg[stock_name] = self.getAverage(self._AMOUNTDAYS,stock_name)
            stock_amount = 1 #for testing purposes buy/sell only one for now
            buy_range = self._PERCENTAGE*self._total_avg[stock_name]
            stock_price = float(stock_price)
            if stock_price > buy_range+self._total_avg[stock_name]:
                decision.append({stock_name: [2, stock_amount]})  #0 is nothing, 1 is buy, 2 is sell
            elif stock_price < -1*buy_range+self._total_avg[stock_name]:
                decision.append({stock_name: [1, stock_amount]})  #0 is nothing, 1 is buy, 2 is sell
            else:
                decision.append({stock_name: [0,0]})
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
