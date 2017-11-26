#! /usr/bin/env python
from time import sleep

try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error importing RPi.GPIO")

GPIO.setmode(GPIO.BOARD)

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
        
