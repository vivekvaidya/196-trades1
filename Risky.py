class Risky:
    stock_counts = {}  # Keys will be stock names; values will be the number of stocks we currently hold
    MAX_STOCKS = 42
    def risk(self, name, amount, buySell):
        if name not in self.stock_counts:
            self.stock_counts[name] = 0

        # Series of tests to determine when not to sell
        if buySell != 1:
            if self.stock_counts[name] - amount < 0:
                return False
            elif amount > self.MAX_STOCKS*3/2:
                return False
            else:
                return True

        # Series of tests to determine when not to buy
        if buySell == 1:
            if self.stock_counts[name] + amount > self.MAX_STOCKS:
                return False
            elif amount > self.MAX_STOCKS*3/2:
                return False
            else:
                return True
