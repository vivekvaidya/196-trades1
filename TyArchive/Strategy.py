class Strategy:
    total_avg = {}
    counter = 0
    PERCENTAGE = .25
    def mean_strategy(self,datum):
        """Uses mean reversion to decide if to buy, sell, or do nothing.
        Datum is what is returned by a yahoo finance api call on stocks. """
        decision = []
        self.counter +=1
        for stock in datum["query"]["results"]["quote"]:
            stock_price = stock["Ask"]
            stock_name = stock["symbol"]
            if self.total_avg.get(stock_name) != None:
                self.total_avg[stock_name] = (self.total_avg[stock_name]*(self.counter-1)+float(stock_price))/(self.counter) #updating the average value
            else:
                self.total_avg[stock_name] = float(stock_price)
  #          self.total_avg[stock_name] = float(stock["PreviousClose"])
            high = float(stock["DaysHigh"])
            low = float(stock["DaysLow"])
            days_range = high - low
            stock_amount = 1 #for testing purposes buy/sell only one for now
            buy_range = self.PERCENTAGE*days_range
            stock_price = float(stock_price)
            if stock_price > buy_range/2+self.total_avg[stock_name]:
                decision.append({stock_name: [2, stock_amount]})  #0 is nothing, 1 is buy, 2 is sell
            elif stock_price < -1*buy_range/2+self.total_avg[stock_name]:
                decision.append({stock_name: [1, stock_amount]})  #0 is nothing, 1 is buy, 2 is sell
            else:
                decision.append({stock_name: [0,0]})
        return decision
    
