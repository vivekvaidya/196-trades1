#!/bin/env python2.6
import json
import time
import calendar
dataFinal = {}
import matplotlib.pyplot as plt
from Strategy import *
stuff = []
stamps = []
with open("filed.json","r") as tsla:
    amount = 1000
    strat = Strategy(amount)
    print "Start with $"+str(amount)
    final_val = 0
    for i in enumerate(tsla):
	try:
            data = json.loads(i[1]) #figure out later
	except ValueError:
	    pass
        strat.mean_strategy(data)
        timeStamp = data["query"]["created"]
        timeStamp = calendar.timegm(time.strptime(timeStamp,"%Y-%m-%dT%H:%M:%SZ"))
       # print strat.mean_strategy(data)
        final_val = data
    strat.sellAll(data)
    print "Ended with $"+str(strat.printDatMoney())
