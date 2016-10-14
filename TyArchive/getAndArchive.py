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

with open("TeslaData.json","a") as tsla, open("FordData.json","a") as ford, open("GMData.json","a") as gm:
    while True: 
        tData = getDataJson(["TSLA","Ford","GM"])
        counter = 0
        for each in tData["query"]["results"]["quote"]:
            if each is not None:
                if counter %3 == 0:
                    json.dump(each,tsla) 
                    tsla.write("\n")
                elif counter % 3  == 1:
                    json.dump(each,ford) 
                    ford.write("\n")
                else:
                    json.dump(each,gm) 
                    gm.write("\n")
            counter+=1
        
        time.sleep(2)
