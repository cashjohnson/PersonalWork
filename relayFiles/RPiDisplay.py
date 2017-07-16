#! /usr/bin/env python2
from time import sleep

try:
	import RPi.GPIO as GPIO
except RuntimeError:
	print 'Error importing RPi.GPIO'

GPIO.setMode(GPIO.BOARD)

# TODO: assign the pins correctly to the board pins
#Pin mapping from Arduino to the ATmega DIP28 if you need it
# http://www.arduino.cc/en/Hacking/PinMapping
digit1 = 36; #PWM Display pin 1
digit2 = 37; #PWM Display pin 2
digit3 = 38; #PWM Display pin 6
digit4 = 40; #PWM Display pin 8
segA = 6; #Display pin 14
segB = 7; #Display pin 16
segC = 8; #Display pin 13
segD = 9; #Display pin 3
segE = 10; #Display pin 5
segF = 11; #Display pin 11
segG = 12; #Display pin 15

DP = 13; #Display pin 7

 # TODO: relist these
outputList = [digit1,digit2,digit3,digit4]#,segA,segB,segC,segD,segE,segF,segG,DP]

GPIO.setup(outputList,GPIO.OUT)

for j in range(0,4):
    print 'Cycle:' + repr(j)
    for i in outputList:
        GPIO.output(i,GPIO.LOW)
        print repr(i) + ':LOW'
        sleep(0.5)
    for i in outputList:
        GPIO.output(i,GPIO.HIGH)
        print repr(i) + ':LOW'
        sleep(0.5)

GPIO.cleanup()

# def displayString(toDisplay):
# 	DISPLAY_BRIGHTNESS = 0.5
# 	DIGIT_ON = 'HIGH'
# 	DIGIT_OFF = 'LOW'

# while true:
# 	displayString('12.34')