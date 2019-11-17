read = open("stock-view.txt", "r+")
print(read)
data = read.readlines()
stockName = input("Name a stock. Type 'End' to quit.")
while stockName != "End":
      stockName = input("Name a stock. Type 'End' to quit.")
print(data)


