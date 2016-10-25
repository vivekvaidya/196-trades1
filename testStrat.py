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
    strat = Strategy()
    for i in enumerate(tsla):
	try:
            data = json.loads(i[1]) #figure out later
	except ValueError:
	    pass
        timeStamp = data["query"]["created"]
        timeStamp = calendar.timegm(time.strptime(timeStamp,"%Y-%m-%dT%H:%M:%SZ"))
        print strat.mean_strategy(data)
