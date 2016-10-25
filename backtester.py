import json
import time
import calendar
import matplotlib.pyplot as plt
import collections

TslaAskPrice = []
TslaVolume=[]
TslaFiftyDay=[]
TslaTwoHundredDay=[]

VTIAskPrice = []
VTIVolume=[]
VTIFiftyDay=[]
VTITwoHundredDay=[]

VIXAskPrice = []
VIXVolume=[]
VIXFiftyDay=[]
VIXTwoHundredDay=[]

stamps = []

with open("filed.json","r") as filed:

    for i in enumerate(filed):
	try:
        	data = json.loads(i[1])
	except ValueError:
		pass
        timeStamp = data["query"]["created"]
        timeStamp = calendar.timegm(time.strptime(timeStamp,"%Y-%m-%dT%H:%M:%SZ"))
        stamps.append(timeStamp)

        TslaAskPrice.append(data["query"]["results"]["quote"][0]["Ask"])
        TslaVolume.append(data["query"]["results"]["quote"][0]["Volume"])
        TslaFiftyDay.append(data["query"]["results"]["quote"][0]["FiftydayMovingAverage"])
        VTITwoHundredDay.append(data["query"]["results"]["quote"][0]["TwoHundreddayMovingAverage"])

        VTIAskPrice.append(data["query"]["results"]["quote"][1]["Ask"])
        VTIVolume.append(data["query"]["results"]["quote"][1]["Volume"])
        VTIFiftyDay.append(data["query"]["results"]["quote"][1]["FiftydayMovingAverage"])
        VTIAskPrice.append(data["query"]["results"]["quote"][1]["TwoHundreddayMovingAverage"])

        VIXAskPrice.append(data["query"]["results"]["quote"][2]["Ask"])
        VIXVolume.append(data["query"]["results"]["quote"][2]["Volume"])
        VIXFiftyDay.append(data["query"]["results"]["quote"][2]["FiftydayMovingAverage"])
        VIXAskPrice.append(data["query"]["results"]["quote"][2]["TwoHundreddayMovingAverage"])


