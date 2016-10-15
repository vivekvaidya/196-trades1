from yahoo_finance import Share
import json
import time
microsoft=Share('MSFT')
with open('data.json','w') as outfile:
    while True:
        data =  microsoft.get_price()
        json.dump(data,outfile)
        sleep(5*60)
        ms.refresh()
        
            
