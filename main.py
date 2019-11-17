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
stockOld=[]
stockChange=[]
clear = lambda: os.system('clear')
clear()

def readConfig():
      global stockNames, data
      read = open("stock-view.txt", "r+")
      data = read.readlines()
      for z in range(0,len(data)):
            stringTemp = data[z]
            data[z]=stringTemp.strip()
            stockNames.append(data[z])
def getStockValue():
      global stockValues, stockNames
      try:
            for i in stockNames:
                  stock = requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol="+i+"&interval=5min&apikey=7S476M9A5A4CILSN").json()
                  with open('refs.json', 'w') as json_file:
                        json.dump(stock, json_file, indent = 4, sort_keys=True)
                  f=open('refs.json', 'r+')
                  #f=open(json.dump(stock, json_file, indent = 4, sort_keys=True), "w+")
                  lines=f.readlines()
                  goodLine = ""
                  for x in lines:
                        if 'open"' in x:              
                              goodLine = x
                              break
                  store=""
                  for y in range(24, 31):
                        store = store + goodLine[y]             
                  stockValues.append(store)
      except IndexError:
            print("Rate Limit Reached. (API Side Error)")
      
def calculateChange():
      global stockValues, stockOld, stockChange
      for x in stockValues:
            
            y=stockValues.index(x)
            stockChange=[]
            print (type((x)))
            print (type(stockOld[y]))
            stockChange.append((float(x))/(float(stockOld[y])))
      
def printStockValue():
      global stockOld
      for x in range(len(stockNames)):
            try: 
                  print(stockNames[x], "-", stockValues[x], "Change:", stockChange[x])
            except IndexError:
                  print(stockNames[x], "-", stockValues[x])
      stockOld = stockValues
      time.sleep(60)
      clear()

getStockValue()
try:
    while True:
      readConfig()
      getStockValue()
      printStockValue() 
      calculateChange()

except KeyboardInterrupt:
    pass
    import requests
    









