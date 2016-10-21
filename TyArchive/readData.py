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
        data = json.loads(i[1]) #figure out later
        timeStamp = data["query"]["created"]
        timeStamp = calendar.timegm(time.strptime(timeStamp,"%Y-%m-%dT%H:%M:%SZ"))
        print strat.mean_strategy(data)
        stamps.append(timeStamp)
        stuff.append(data["query"]["results"]["quote"][0]["Ask"])
        dataFinal[timeStamp] = data["query"]["results"]["quote"][0]["Ask"]

plt.plot(stamps,stuff)
plt.show()
