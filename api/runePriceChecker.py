# Project in Python2
# Source: https://stackoverflow.com/questions/12965203/how-to-get-json-from-webpage-into-python-script
# Source: http://runescape.wikia.com/wiki/Application_programming_interface

# Problem: I have recently been playing around with Runescape again (just for nostalgia's sake) and ran
# into the problem that I was short on money and wanted an easy way to make it! According to this link
# http://runescape.wikia.com/wiki/Money_making_guide/Buying_runes I would be able to make a nice sum in a short
# amount of time depending on the market. Being lazy and assuming I might do this multiple times I decided to make
# a tool that would tell me where/which runes to buy from vendors and sell on the Grand Exchange (a central 
# auction house in the game).

# items
# print(data)
# print(data["items"][0]["name"])
# print()
# print(data["items"][0]["current"]["price"])

# detail
# print(data["item"]["current"])

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

def standardPriceCheck():
    print("")
    if (fireRune.currentPrice > 17):
        print("Buy Fire Runes")
    if (waterRune.currentPrice > 17):
        print("Buy Water Runes")
    if (airRune.currentPrice > 17):
        print("Buy Air Runes")
    if (earthRune.currentPrice > 17):
        print("Buy Earth Runes")
    if (mindRune.currentPrice > 17):
        print("Buy Mind Runes")
    if (bodyRune.currentPrice > 16):
        print("Buy Body Runes")
    if (chaosRune.currentPrice > 140):
        print("Buy Chaos Rune")
    if (deathRune.currentPrice > 310):
        print("Buy Death Rune")
    print("")
    raw_input("Press Enter to continue...")
    print("")

print("Downloading Values from Runescape API!")


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

# airRune.showValues()
# bodyRune.showValues()
# earthRune.showValues()
# fireRune.showValues()
# waterRune.showValues()
# mindRune.showValues()
# cosmicRune.showValues()
# chaosRune.showValues()
# natureRune.showValues()
# lawRune.showValues()
# deathRune.showValues()
# astralRune.showValues()
# bloodRune.showValues()
# soulRune.showValues()
print("")

#1 Carwen Essencebinder Magical Runes Shop
print("Teleport to the Burthrope lodestone, run east to Carwen Essencebinder Magical Runes Shop")
standardPriceCheck()

#2 Aubury's Rune Shop
print("Teleport to the Varrock lodestone, run north-east to Aubury's Rune Shop")
standardPriceCheck()

#3 Ali's Discount Wares
# print("Teleport to the Al Kharid lodestone, run north to Ali's Discount Wares")
# print("Opening Ali's rune shop requires talking to him and selecting the appropriate dialogue options (\"I would like to have a look at your selection of runes.\" and \"Buy elemental runes.\")")

#4 Betty's Magic Emporium
print("Teleport to the Port Sarim lodestone, run north to Betty's Magic Emporium (located in the northernmost house in Port Sarim)")
standardPriceCheck()

#5 Void Knight Magic Store
print("From Betty's shop, run south to the second-southernmost pier at the Port Sarim docks, and click on the Squire to travel to the Void Knights' Outpost. From your arrival spot in the outpost run south-west to the Void Knight Magic Store")
standardPriceCheck()

#6 Magic Guild Store - Runes and Staves
print("Teleport to the Yanille lodestone, run east to the Magic Guild, go up the stairs to the second floor where Magic Guild Store - Runes and Staves is located")
standardPriceCheck()

#7 Baba Yaga's Magic Shop
print("Teleport to the Lunar Isle lodestone, click the walking house to the north to enter it and reach Baba Yaga who runs the Baba Yaga's Magic Shop")
standardPriceCheck()

#8 Ape Atoll
print("Travel to Ape Atoll either by casting the Teleport to Ape Atoll spell or by other means, equip a greegree, and run to Tutab's Magical Market, located in the southern part of the marketplace")
standardPriceCheck()

#9 Edgeville
print("Teleport to the Edgeville lodestone, bank all your items, and run north to the Mage of Zamorak's shop Battle Runes, located in level 5 Wilderness")
standardPriceCheck()

#10 Wilderness! D=
print("Return to Edgeville and bank all your items. Make sure you have a knife in your tool belt or are carrying a slashing weapon. Head south to the ruined building in Edgeville and travel to level 51 Wilderness by pulling the Edgeville teleport lever. Exit the Deserted Keep you find yourself in by cutting through the cobweb blocking the way north, and head west to a small ruined building north of the Mage Arena. Cut through the two cobwebs blocking the way and pull the lever to be transported to the small cave where Lundail runs his Arena-side Rune Shop. This is a safe area that isn't considered Wilderness and also contains a bank, so you may purchase the runes from the shop in peace.")
print("")
if (fireRune.currentPrice > 17):
    print("Buy Fire Runes")
if (waterRune.currentPrice > 17):
    print("Buy Water Runes")
if (airRune.currentPrice > 17):
    print("Buy Air Runes")
if (earthRune.currentPrice > 17):
    print("Buy Earth Runes")
if (mindRune.currentPrice > 17):
    print("Buy Mind Runes")
if (bodyRune.currentPrice > 16):
    print("Buy Body Runes")
if (natureRune.currentPrice > 372):
    print("Buy Nature Rune")
if (chaosRune.currentPrice > 140):
    print("Buy Chaos Rune")
if (lawRune.currentPrice > 378):
    print("Buy Law Rune")
if (cosmicRune.currentPrice > 232):
    print("Buy Cosmic Rune")
if (deathRune.currentPrice > 310):
    print("Buy Death Rune")
print("")
raw_input("Press Enter to continue...")
print("")
print("Go make some bank!")