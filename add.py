config = open("stock-view.txt", "w+")
stockName = input("Name a stock. Type 'End' to quit.")
while stockName != "End":
      config.write(stockName+"\n")
      stockName = input("Name a stock. Type 'End' to quit.")