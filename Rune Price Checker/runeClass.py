#!/usr/bin/env python
from urllib import request
import json


class Runes:
    apiUrl = ""
    apiIndex = ""
    currentPrice = 0
    name = ""

    # def __init__(self, url, apiIndex):
    #     self.apiUrl = url
    #     self.apiIndex = apiIndex
    #     response = request.urlopen(self.apiUrl)
    #     data = json.loads(response.read())
    #     self.name = data["items"][self.apiIndex]["name"]
    #     self.currentPrice = data["items"][self.apiIndex]["current"]["price"]

    def __init__(self, url, name):
        self.apiUrl = url
        self.name = name
        response = request.urlopen(self.apiUrl)
        data = json.loads(response.read())
        for i in range(0, len(data["items"])):
            if data["items"][i]["name"] == name:
                self.currentPrice = data["items"][i]["current"]["price"]
                self.apiIndex = i
                break
        if type(self.currentPrice) == str:
            self.currentPrice = self.currentPrice.replace(',', '')
            self.currentPrice = int(self.currentPrice)

    def showValues(self):
        print('This is %s' % self.name)
        print('The apiIndex = %s' % self.apiIndex)
        print('The current price = %d' % self.currentPrice)
        print('')
