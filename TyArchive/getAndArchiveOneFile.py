import requests
import json
import time
def getDataJson(name):
    totalName = ''
    for x in name:
        totalName+='"'+str(x)+'",'
    totalName= totalName[:len(totalName)-1]
    data = requests.get("http://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20yahoo.finance.quotes%20where%20symbol%20in%20("+totalName+")%0A%09%09&env=http%3A%2F%2Fdatatables.org%2Falltables.env&format=json")
    if data.status_code == 200: 
        data = data.json()
    else:
        data = None
    return data

with open("filed.json","w") as filed:
    counter = 0
    while True: 
        js = getDataJson(["TSLA","Ford","GM"])
        if js is not None:
            json.dump(js,filed) 
            filed.write("\n")
            counter+=1
            print counter
        time.sleep(2)
