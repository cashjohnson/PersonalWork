from runeClass import *

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


def standard_price_check():
    print("")
    if fireRune.currentPrice > 17:
        print("Buy Fire Runes")
    if waterRune.currentPrice > 17:
        print("Buy Water Runes")
    if airRune.currentPrice > 17:
        print("Buy Air Runes")
    if earthRune.currentPrice > 17:
        print("Buy Earth Runes")
    if mindRune.currentPrice > 17:
        print("Buy Mind Runes")
    if bodyRune.currentPrice > 16:
        print("Buy Body Runes")
    if chaosRune.currentPrice > 140:
        print("Buy Chaos Rune")
    if deathRune.currentPrice > 310:
        print("Buy Death Rune")
    print("")

def wildnerness_price_check():
    print("")
    if fireRune.currentPrice > 17:
        print("Buy Fire Runes")
    if waterRune.currentPrice > 17:
        print("Buy Water Runes")
    if airRune.currentPrice > 17:
        print("Buy Air Runes")
    if earthRune.currentPrice > 17:
        print("Buy Earth Runes")
    if mindRune.currentPrice > 17:
        print("Buy Mind Runes")
    if bodyRune.currentPrice > 16:
        print("Buy Body Runes")
    if natureRune.currentPrice > 372:
        print("Buy Nature Rune")
    if chaosRune.currentPrice > 140:
        print("Buy Chaos Rune")
    if lawRune.currentPrice > 378:
        print("Buy Law Rune")
    if cosmicRune.currentPrice > 232:
        print("Buy Cosmic Rune")
    if deathRune.currentPrice > 310:
        print("Buy Death Rune")
    print("")

print("Downloading values from Runescape API!")
print('0/14')
airRune = Runes(urlAirRune, 'Air rune')
print('1/14')
bodyRune = Runes(urlBodyRune, 'Body rune')
print('2/14')
earthRune = Runes(urlEarthRune, 'Earth rune')
print('3/14')
fireRune = Runes(urlFireRune, 'Fire rune')
print('4/14')
waterRune = Runes(urlWaterRune, 'Water rune')
print('5/14')
mindRune = Runes(urlMindRune, 'Mind rune')
print('6/14')
cosmicRune = Runes(urlCosmicRune, 'Cosmic rune')
print('7/14')
chaosRune = Runes(urlChaosRune, 'Chaos rune')
print('8/14')
natureRune = Runes(urlNatureRune, 'Nature rune')
print('9/14')
lawRune = Runes(urlLawRune, 'Law rune')
print('10/14')
deathRune = Runes(urlDeathRune, 'Death rune')
print('11/14')
astralRune = Runes(urlAstralRune, 'Astral rune')
print('12/14')
bloodRune = Runes(urlBloodRune, 'Blood rune')
print('13/14')
soulRune = Runes(urlSoulRune, 'Soul rune')
print('14/14')

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
# print("")

standard_price_check()

# 1 Carwen Essencebinder Magical Runes Shop
print("Teleport to the Burthrope lodestone, run east to Carwen Essencebinder Magical Runes Shop\n")

# 2 Aubury's Rune Shop
print("Teleport to the Varrock lodestone, run north-east to Aubury's Rune Shop\n")

# 3 Ali's Discount Wares
print("Teleport to the Al Kharid lodestone, run north to Ali's Discount Wares")
print("Opening Ali's rune shop requires talking to him and selecting the appropriate dialogue options (\"I would like to have a look at your selection of runes.\" and \"Buy elemental runes.\"\n)")

# 4 Betty's Magic Emporium
print(
    "Teleport to the Port Sarim lodestone, run north to Betty's Magic Emporium (located in the northernmost house in Port Sarim)\n")

# 5 Void Knight Magic Store
print(
    "From Betty's shop, run south to the second-southernmost pier at the Port Sarim docks, and click on the Squire to travel to the Void Knights' Outpost. From your arrival spot in the outpost run south-west to the Void Knight Magic Store\n")

# 6 Magic Guild Store - Runes and Staves
print(
    "Teleport to the Yanille lodestone, run east to the Magic Guild, go up the stairs to the second floor where Magic Guild Store - Runes and Staves is located\n")

# 7 Baba Yaga's Magic Shop
print(
    "Teleport to the Lunar Isle lodestone, click the walking house to the north to enter it and reach Baba Yaga who runs the Baba Yaga's Magic \n")

# 8 Ape Atoll
print(
    "Travel to Ape Atoll either by casting the Teleport to Ape Atoll spell or by other means, equip a greegree, and run to Tutab's Magical Market, located in the southern part of the marketplace\n")

# 9 Edgeville
print(
    "Teleport to the Edgeville lodestone, bank all your items, and run north to the Mage of Zamorak's shop Battle Runes, located in level 5 Wilderness\n")

# 10 Wilderness! D=
wildnerness_price_check()
print(
    "Return to Edgeville and bank all your items. Make sure you have a knife in your tool belt or are carrying a slashing weapon. Head south to the ruined building in Edgeville and travel to level 51 Wilderness by pulling the Edgeville teleport lever. Exit the Deserted Keep you find yourself in by cutting through the cobweb blocking the way north, and head west to a small ruined building north of the Mage Arena. Cut through the two cobwebs blocking the way and pull the lever to be transported to the small cave where Lundail runs his Arena-side Rune Shop. This is a safe area that isn't considered Wilderness and also contains a bank, so you may purchase the runes from the shop in peace.\n")
print("Go make some bank!")
input()
