import webbrowser
import requests
import json
import time
import os
from os import system
import configparser
import re
stockNames=[]
stockValues=[]
symbol = 'tmp'
clear = lambda: os.system('clear')
clear()

def readConfig():
      global stockNames, data
      read = open("stock-view.txt", "r+")
      data = read.readlines()
      for i in range(0,len(data)):
            stringTemp = data[i]
            data[i]=stringTemp.strip()
            stockNames.append(data[i])
def getStockValue():
      global stockValues, stockNames
      for i in stockNames:
            stock = requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol="+i+"&interval=1min&datatype=json&apikey=F9S5UGUIMIOGNM0P")
            with open('kai.txt', 'w') as outfile:
                  json.dump(stock.json(), outfile, sort_keys = True, indent = 4, ensure_ascii = False)
            f=open('kai.txt', 'r+')
            lines=f.readlines()
            goodLine = ""
            for x in lines:
                  if 'open"' in x:              
                        goodLine = x
                        break
            store=""
            for x in range(24, 32):
                  store = store + goodLine[x]
            stockValues.append(store)
      
def printStockValue():
      for x in range(len(stockNames)):
            print(stockNames[x], "-", stockValues[x])
      time.sleep(60)
      clear()

getStockValue()
#print(req)

#read config
#configparser = configparser.RawConfigParser()   
 #configFilePath = r''
 #configParser.read(configFilePath)
try:
    while True:
      readConfig()
      print(data)
      getStockValue()
      printStockValue() 

except KeyboardInterrupt:
    pass
    import requests
    









