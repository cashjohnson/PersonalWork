#! /usr/bin/env python2
from time import sleep
import os
try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error importing RPi.GPIO")
import RPiDisplay
import tempSensor

GPIO.setmode(GPIO.BOARD)

digit1 = 3 #PWM Display pin 1
digit2 = 5 #PWM Display pin 2
digit3 = 8 #PWM Display pin 6
digit4 = 10 #PWM Display pin 8
segA = 11 #Display pin 14
segB = 12 #Display pin 16
segC = 13 #Display pin 13
segD = 15 #Display pin 3
segE = 16 #Display pin 5
segF = 18 #Display pin 11
segG = 19 #Display pin 15
#DP = 21 #Display pin 7
displayList = [digit1,digit2,digit3,digit4,segA,segB,segC,segD,segE,segF,segG]
GPIO.setup(displayList,GPIO.OUT)

rel1 = 40
rel2 = 38
rel3 = 37
rel4 = 36
rel5 = 35
rel6 = 33
rel7 = 32
rel8 = 31
rel9 = 29
rel10 = 28
rel11 = 27
rel12 = 26
rel13 = 24
rel14 = 23
rel15 = 22
rel16 = 21
relayList = [rel1,rel2,rel3,rel4,rel5,rel6,rel7,rel8,rel9,rel10,rel11,rel12,rel13,rel14,rel15,rel16]
GPIO.setup(relayList,GPIO.OUT)

def RPiControlDemo():
    SLEEP_TIME = .1
    for j in range(0,2):
        print repr(j) + ':cycle'
        for i in outputList:
            GPIO.output(i,GPIO.LOW)
            print repr(i) + ':LOW'
            sleep(SLEEP_TIME)
        for i in outputList:
            GPIO.output(i,GPIO.HIGH)
            print repr(i) + ':HIGH'
            sleep(SLEEP_TIME)

def relayControl(relayNumber, relayState):
    if relayState == 'ON':
        GPIO.output(relayNumber,GPIO.HIGH)
    elif relayState == 'OFF':
        GPIO.output(relayNumber,GPIO.LOW)

if __name__ == '__main__':
	RPiControlDemo()
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
	GPIO.cleanup()
