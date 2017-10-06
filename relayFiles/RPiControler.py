#! /usr/bin/env python
from time import sleep

try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error importing RPi.GPIO")

GPIO.setmode(GPIO.BOARD)

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
