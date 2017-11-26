#! /usr/bin/env python2
from time import sleep
import os


try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error importing RPi.GPIO")


import RPiDisplay


import tempSensor #Uses pin 7
#Use print(tempSensor.read_temp())

GPIO.setmode(GPIO.BOARD)

#digit1 = 3 #PWM Display pin 1
digit2 = 3 #PWM Display pin 2
digit3 = 5 #PWM Display pin 6
#digit4 = 7 #PWM Display pin 8
segA = 8 #Display pin 14
segB = 10 #Display pin 16
segC = 11 #Display pin 13
segD = 12 #Display pin 3
segE = 13 #Display pin 5
segF = 15 #Display pin 11
segG = 16 #Display pin 15
#DP = 21 #Display pin 7
displayList = [digit2,digit3,segA,segB,segC,segD,segE,segF,segG]
GPIO.setup(displayList,GPIO.OUT)

#Relay Number = RPi Pin
rel1 = 40
rel2 = 38
rel3 = 37
rel4 = 36
rel5 = 35
rel6 = 33
rel7 = 32
rel8 = 31
rel9 = 29
rel10 = 26
rel11 = 24
rel12 = 23
rel13 = 22
rel14 = 21
rel15 = 19
rel16 = 18
relayList = [rel1,rel2,rel3,rel4,rel5,rel6,rel7,rel8,rel9,rel10,rel11,rel12,rel13,rel14,rel15,rel16]
GPIO.setup(relayList,GPIO.OUT)

def relayControl(relayNumber, relayState):
    if relayState == 'ON':
        GPIO.output(relayNumber,GPIO.HIGH)
    elif relayState == 'OFF':
        GPIO.output(relayNumber,GPIO.LOW)

def RPiRelayTest():
    SLEEP_TIME = .4
    for i in range(0,len(relayList)):
        relayControl(relayList[i],'ON')
        print repr(i+1) + ':LOW'
        sleep(SLEEP_TIME)
    for i in range(0,len(relayList)):
        relayControl(relayList[i],'OFF')
        print repr(i+1) + ':HIGH'
        sleep(SLEEP_TIME)



if __name__ == '__main__':
	RPiRelayTest()
	# counter = 0
	# number = tempSensor.read_temp()
	# relayLow = True
	# relayControl(rel1,'OFF')
	# while True:
	#         if counter < 100:
	#             thing = '%.2f' % number
	#             RPiDisplay.displayString(thing)
	#             counter = counter + 1
	#         else:
	#             counter = 0
	#             number = tempSensor.read_temp()
	#             print repr(number)
	# 


	##            if relayLow == True:
	##                RPiControler.relayControl(rel1,'ON')
	##                relayLow = False
	##            elif relayLow == False:
	##                RPiControler.relayControl(rel1,'OFF')
	##                relayLow = True
	print(tempSensor.read_temp())
	GPIO.cleanup()
