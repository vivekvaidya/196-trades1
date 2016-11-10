class Money:
    _money = 0.0
    def __init__(self, starting):
        self._money = starting

    def add(self, amount):
        self._money +=amount

    def remove(self, amount):
        self._money-=amount

    def getMoney(self):
        return self._money
