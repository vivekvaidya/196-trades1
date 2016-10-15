class strat:
    total_avg = {}
    high = {}
    low = {}
    counter = 0

    def mean_strategy(x):
        for num in total_avg:
            total_avg[num] = ((total_avg[num]*counter)+x[num])/(counter+1)
        high = x[days_high]
        low = x[days_low]
        for stock in x:
            if x[stock_price] < 0.25*x[day_range]+total_avg[stock]:
                decision.append({stock: [2, stock_amount]})  #0 is nothing, 1 is buy, 2 is sell
            elif x[stock_price] > 0.25*x[day_range]+total_avg[stock]:
                decision.append({stock: [1, stock_amount]})  #0 is nothing, 1 is buy, 2 is sell
            else:
                decision.append(stock: [0])
        return decision
