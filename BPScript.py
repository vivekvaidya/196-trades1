from urllib2 import Request, urlopen, URLError
import json
import csv
import time

while True:

    request = Request('http://finance.google.com/finance/info?client=ig&q=NYSE:BP')

    try:
        response = urlopen(request)
        lol = response.read()
        y = lol[4::]
        y.replace("\n","")
        x = json.loads(y)[0]
        L = [x["t"], x["l"], x["e"], x["lt"]]
    
        with open('BPDataSecondRun.csv','ab') as mycsvfile:
            temp = csv.writer(mycsvfile)
            temp.writerow(L)
    
    except URLError, e:
        print "error"
    time.sleep(300)
