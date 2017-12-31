# Project in Python2
# Source: https://stackoverflow.com/questions/12965203/how-to-get-json-from-webpage-into-python-script
# Source: http://runescape.wikia.com/wiki/Application_programming_interface

# Problem: I have recently been playing around with Runescape again (just for nostalgia's sake) and ran
# into the problem that I was short on money and wanted an easy way to make it! According to this link
# http://runescape.wikia.com/wiki/Money_making_guide/Buying_runes I would be able to make a nice sum in a short
# amount of time depending on the market. Being lazy and assuming I might do this multiple times I decided to make
# a tool that would tell me where/which runes to buy from vendors and sell on the Grand Exchange (a central 
# auction house in the game).

import json
import urllib

urlAirRune = 'http://services.runescape.com/m=itemdb_rs/api/catalogue/items.json?category=32&alpha=a&page=1'
urlBodyRune = 'http://services.runescape.com/m=itemdb_rs/api/catalogue/items.json?category=32&alpha=b&page=1'
urlEarthRune = 'http://services.runescape.com/m=itemdb_rs/api/catalogue/items.json?category=32&alpha=e&page=1'
urlFireRune = 'http://services.runescape.com/m=itemdb_rs/api/catalogue/items.json?category=32&alpha=f&page=1'
urlWaterRune = 'http://services.runescape.com/m=itemdb_rs/api/catalogue/items.json?category=32&alpha=w&page=1'

urlArray = [urlAirRune,urlBodyRune,urlEarthRune,urlFireRune,urlWaterRune]
apiIndex = [0,2,0,1,1]
prices = []

for i in range(0,len(urlArray)):
    response = urllib.urlopen(urlArray[i])
    data = json.loads(response.read())
    itemName = data["items"][apiIndex[i]]["name"]
    itemPrice = data["items"][apiIndex[i]]["current"]["price"]
    print('%s current GE price is %s gp' % (itemName, itemPrice))
    prices[i] = data["items"][apiIndex[i]]["current"]["price"]

# Carwen Essencebinder Magical Runes Shop
print("Teleport to the Burthrope lodestone, run east to Carwen Essencebinder Magical Runes Shop")


#[GEAirRune,GEBodyRune,GEEarthRune,GEFireRune,GEWaterRune]


# items
# print(data)
# print(data["items"][0]["name"])
# print()
# print(data["items"][0]["current"]["price"])


# detail
# print(data["item"]["current"])

