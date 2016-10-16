class strat:
    total_avg = {}
    counter = 0

    def mean_strategy(datum):
        counter +=1
        for stock in datum:
            stock_price = stock["query"]["results"]["quote"]["Ask"]
            total_avg[stock] = (total_avg[stock]*(counter-1)+stock_price)/(counter) #updating the average value
            high = stock["query"]["results"]["quote"]["daysHigh"]
            low = stock["query"]["results"]["quote"]["daysLow"]
            days_range = high - low
            stock_amount = 1 #for testing purposes buy/sell only one for now
            if stock_price < (0.25*days_range+total_avg[stock]):
                decision.append({stock: [2, stock_amount]})  #0 is nothing, 1 is buy, 2 is sell
            elif stock_price > (0.25*days_range+total_avg[stock]):
                decision.append({stock: [1, stock_amount]})  #0 is nothing, 1 is buy, 2 is sell
            else:
                decision.append({stock: [0,0]})
        return decision

