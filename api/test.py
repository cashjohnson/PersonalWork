#! python3

import requests
import json
import urllib2


data = json.load(urllib2.urlopen('http://services.runescape.com/m=itemdb_rs/api/catalogue/detail.json?item=21787')

print(data.text)
