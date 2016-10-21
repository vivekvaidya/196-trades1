import json
import time
import calendar
import matplotlib.pyplot as plt
askPrice = []
volume=[]
fiftyDay=[]
TwoHundredDay=[]
stamps = []
with open("filed.json","r") as tsla:
    for i in enumerate(tsla):
        data = json.loads(i[1])
        timeStamp = data["query"]["created"]
        timeStamp = calendar.timegm(time.strptime(timeStamp,"%Y-%m-%dT%H:%M:%SZ"))
        stamps.append(timeStamp)
        askPrice.append(data["query"]["results"]["quote"][0]["Ask"])
        volume.append(data["query"]["results"]["quote"][0]["Volume"])
        fiftyDay.append(data["query"]["results"]["quote"][0]["FiftydayMovingAverage"])
        TwoHundredDay.append(data["query"]["results"]["quote"][0]["TwoHundreddayMovingAverage"])

plt.title("Asking Price")
plt.plot(stamps,askPrice)
plt.show()
plt.title("Volume")
plt.plot(stamps,volume)
plt.show()
plt.title("Fifty Day")
plt.plot(stamps,fiftyDay)
plt.show()
plt.title("Two Hundred Day")
plt.plot(stamps,TwoHundredDay)
plt.show()
