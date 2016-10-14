import json
import time
import calendar
dataFinal = {}
import matplotlib.pyplot as plt
stuff = []
stamps = []
with open("TeslaData.json","r") as tsla:
    for i in enumerate(tsla):
        
        data = json.loads(i[1])
        timeStamp = data["query"]["created"]
        timeStamp = calendar.timegm(time.strptime(timeStamp,"%Y-%m-%dT%H:%M:%SZ"))
        stamps.append(timeStamp)
        stuff.append(data["query"]["results"]["quote"]["Ask"])

        #dataFinal[timeStamp] = data["query"]["results"]["quote"]["Ask"]

plt.plot(stamps,stuff)
plt.show()
