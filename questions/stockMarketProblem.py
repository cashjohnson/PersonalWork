# This is a problem I found on the internet which caught my eye. If we recoreded the price of a stock
# at regular intervals and converted it to a string input (which i made up in textInput) where would be the 
# most money I could make based on the buy and sell price. 

textInput = "65 12 40 12 56 12 45 78 69 51 68 35 78 18 98 68 48 55 68 78 99 48 78 25 68"#random string of inputs 
values = textInput.split()#turning the string input into an array for ease of use

bestBuyIndex = 1#setting an arbitrary starting place at the beginning
bestSellIndex = 2
bestPrice = int(values[2]) - int(values[1])

for i in range(1,len(values)):#iterate through possible buy locations
    for j in range(2,len(values)):#iterate through possible sell locations
    	if (int(values[j])-int(values[i]) > bestPrice):#switching the indexes to reflect the newest best prices
    		bestBuyIndex = int(values[i])
    		bestSellIndex = int(values[j])
    		bestPrice = int(values[j]) - int(values[i])

print "The most money you could make is %d buying at %d and selling at %d"%(bestPrice, bestBuyIndex, bestSellIndex)
