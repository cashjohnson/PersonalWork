#! /usr/bin/env python2
from time import sleep
import os
try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error importing RPi.GPIO")
import RPiControler
import RPiDisplay

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

temp_sensor = '/sys/bus/w1/devices/28-000008aa22ab/w1_slave'

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
DP = 21 #Display pin 7
displayList = [digit1,digit2,digit3,digit4,segA,segB,segC,segD,segE,segF,segG,DP]
GPIO.setup(displayList,GPIO.OUT)

rel1 = 40
rel2 = 38
rel3 = 37
rel4 = 36
relayList = [rel1,rel2,rel3,rel4]
GPIO.setup(relayList,GPIO.OUT)

counter = 0
while counter < 100:
	displayString('88.88')
	counter = counter + 1
RPiControlDemo()

GPIO.cleanup()