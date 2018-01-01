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
urlMindRune = 'http://services.runescape.com/m=itemdb_rs/api/catalogue/items.json?category=32&alpha=m&page=1'
urlCosmicRune = 'http://services.runescape.com/m=itemdb_rs/api/catalogue/items.json?category=32&alpha=c&page=1'
urlChaosRune = 'http://services.runescape.com/m=itemdb_rs/api/catalogue/items.json?category=32&alpha=c&page=1'
urlNatureRune = 'http://services.runescape.com/m=itemdb_rs/api/catalogue/items.json?category=32&alpha=n&page=1'
urlLawRune = 'http://services.runescape.com/m=itemdb_rs/api/catalogue/items.json?category=32&alpha=l&page=1'
urlDeathRune = 'http://services.runescape.com/m=itemdb_rs/api/catalogue/items.json?category=32&alpha=d&page=1'
urlAstralRune = 'http://services.runescape.com/m=itemdb_rs/api/catalogue/items.json?category=32&alpha=a&page=1'
urlBloodRune = 'http://services.runescape.com/m=itemdb_rs/api/catalogue/items.json?category=32&alpha=b&page=1'
urlSoulRune = 'http://services.runescape.com/m=itemdb_rs/api/catalogue/items.json?category=32&alpha=s&page=1'

class Runes:
    apiUrl = ""
    apiIndex = ""
    currentPrice = 0
    name = ""

    def __init__(self, url, apiIndex):
        self.apiUrl = url
        self.apiIndex = apiIndex
        response = urllib.urlopen(self.apiUrl)
        data = json.loads(response.read())
        self.name = data["items"][self.apiIndex]["name"]
        self.currentPrice = data["items"][self.apiIndex]["current"]["price"]

    def extractValues(self):
        response = urllib.urlopen(self.apiUrl)
        data = json.loads(response.read())
        self.name = data["items"][self.apiIndex]["name"]
        self.currentPrice = data["items"][self.apiIndex]["current"]["price"]  

    def showValues(self):
        print('This is %s' % self.name)
        print('The apiIndex = %s' % self.apiIndex)
        print('The current price = %d' % self.currentPrice)
        print('')

airRune = Runes(urlAirRune, 0)
bodyRune = Runes(urlBodyRune, 2)
earthRune = Runes(urlEarthRune, 0)
fireRune = Runes(urlFireRune, 1)
waterRune = Runes(urlWaterRune, 1)
mindRune = Runes(urlMindRune, 1)
cosmicRune = Runes(urlCosmicRune, 3)
chaosRune = Runes(urlChaosRune, 2)
natureRune = Runes(urlNatureRune, 0)
lawRune = Runes(urlLawRune, 2)
deathRune = Runes(urlDeathRune, 2)
astralRune = Runes(urlAstralRune, 3)
bloodRune = Runes(urlBloodRune, 1)
soulRune = Runes(urlSoulRune, 3)

airRune.showValues()
bodyRune.showValues()
earthRune.showValues()
fireRune.showValues()
waterRune.showValues()
mindRune.showValues()
cosmicRune.showValues()
chaosRune.showValues()
natureRune.showValues()
lawRune.showValues()
deathRune.showValues()
astralRune.showValues()
bloodRune.showValues()
soulRune.showValues()

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

