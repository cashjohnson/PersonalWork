#! /usr/bin/env python2
from time import sleep

try:
	import RPi.GPIO as GPIO
except RuntimeError:
	print 'Error importing RPi.GPIO'

GPIO.setmode(GPIO.BOARD)

#Pin mapping from Arduino to the ATmega DIP28 if you need it
# http://www.arduino.cc/en/Hacking/PinMapping
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

outputList = [digit1,digit2,digit3,digit4,segA,segB,segC,segD,segE,segF,segG,DP]

GPIO.setup(outputList,GPIO.OUT)

# for j in range(0,4):
#     print 'Cycle:' + repr(j)
#     for i in outputList:
#         GPIO.output(i,GPIO.LOW)
#         print repr(i) + ':LOW'
#         sleep(0.5)
#     for i in outputList:
#         GPIO.output(i,GPIO.HIGH)
#         print repr(i) + ':HIGH'
#         sleep(0.5)

# GPIO.cleanup()

def displayString(toDisplay):
	DISPLAY_BRIGHTNESS = 0.01
	DIGIT_ON = GPIO.HIGH
	DIGIT_OFF = GPIO.LOW
    
    for i in range(0,5):
        if i==0:
            digitalWrite(digit1,DIGIT_ON)
        elif i==1:
            digitalWrite(digit2, DIGIT_ON)
        elif i==2:
            digitalWrite(digit2, DIGIT_ON)
        elif i==3:
            digitalWrite(digit3, DIGIT_ON)
        elif i==4:
            digitalWrite(digit4, DIGIT_ON)

        lightNumber(toDisplay[i])
        sleep(DISPLAY_BRIGHTNESS)
        lightNumber('10')

        digitalWrite(digit1, DIGIT_OFF)
        digitalWrite(digit2, DIGIT_OFF)
        digitalWrite(digit3, DIGIT_OFF)
        digitalWrite(digit4, DIGIT_OFF)

def lightNumber(numberToDisplay):
    SEGMENT_ON = GPIO.LOW
    SEGMENT_OFF = GPIO.HIGH

    if numberToDisplay=='0':
      digitalWrite(segA, SEGMENT_ON)
      digitalWrite(segB, SEGMENT_ON)
      digitalWrite(segC, SEGMENT_ON)
      digitalWrite(segD, SEGMENT_ON)
      digitalWrite(segE, SEGMENT_ON)
      digitalWrite(segF, SEGMENT_ON)
      digitalWrite(segG, SEGMENT_OFF)
      digitalWrite(DP, SEGMENT_OFF)

    elif numberToDisplay=='1':
      digitalWrite(segA, SEGMENT_OFF)
      digitalWrite(segB, SEGMENT_ON)
      digitalWrite(segC, SEGMENT_ON)
      digitalWrite(segD, SEGMENT_OFF)
      digitalWrite(segE, SEGMENT_OFF)
      digitalWrite(segF, SEGMENT_OFF)
      digitalWrite(segG, SEGMENT_OFF)
      digitalWrite(DP, SEGMENT_OFF)

    elif numberToDisplay=='2':
      digitalWrite(segA, SEGMENT_ON)
      digitalWrite(segB, SEGMENT_ON)
      digitalWrite(segC, SEGMENT_OFF)
      digitalWrite(segD, SEGMENT_ON)
      digitalWrite(segE, SEGMENT_ON)
      digitalWrite(segF, SEGMENT_OFF)
      digitalWrite(segG, SEGMENT_ON)
      digitalWrite(DP, SEGMENT_OFF)

    elif numberToDisplay=='3':
      digitalWrite(segA, SEGMENT_ON)
      digitalWrite(segB, SEGMENT_ON)
      digitalWrite(segC, SEGMENT_ON)
      digitalWrite(segD, SEGMENT_ON)
      digitalWrite(segE, SEGMENT_OFF)
      digitalWrite(segF, SEGMENT_OFF)
      digitalWrite(segG, SEGMENT_ON)
      digitalWrite(DP, SEGMENT_OFF)

    elif numberToDisplay=='4':
      digitalWrite(segA, SEGMENT_OFF)
      digitalWrite(segB, SEGMENT_ON)
      digitalWrite(segC, SEGMENT_ON)
      digitalWrite(segD, SEGMENT_OFF)
      digitalWrite(segE, SEGMENT_OFF)
      digitalWrite(segF, SEGMENT_ON)
      digitalWrite(segG, SEGMENT_ON)
      digitalWrite(DP, SEGMENT_OFF)

    elif numberToDisplay=='5':
      digitalWrite(segA, SEGMENT_ON)
      digitalWrite(segB, SEGMENT_OFF)
      digitalWrite(segC, SEGMENT_ON)
      digitalWrite(segD, SEGMENT_ON)
      digitalWrite(segE, SEGMENT_OFF)
      digitalWrite(segF, SEGMENT_ON)
      digitalWrite(segG, SEGMENT_ON)
      digitalWrite(DP, SEGMENT_OFF)

    elif numberToDisplay=='6':
      digitalWrite(segA, SEGMENT_ON)
      digitalWrite(segB, SEGMENT_OFF)
      digitalWrite(segC, SEGMENT_ON)
      digitalWrite(segD, SEGMENT_ON)
      digitalWrite(segE, SEGMENT_ON)
      digitalWrite(segF, SEGMENT_ON)
      digitalWrite(segG, SEGMENT_ON)
      digitalWrite(DP, SEGMENT_OFF)

    elif numberToDisplay=='7':
      digitalWrite(segA, SEGMENT_ON)
      digitalWrite(segB, SEGMENT_ON)
      digitalWrite(segC, SEGMENT_ON)
      digitalWrite(segD, SEGMENT_OFF)
      digitalWrite(segE, SEGMENT_OFF)
      digitalWrite(segF, SEGMENT_OFF)
      digitalWrite(segG, SEGMENT_OFF)
      digitalWrite(DP, SEGMENT_OFF)

    elif numberToDisplay=='8':
      digitalWrite(segA, SEGMENT_ON)
      digitalWrite(segB, SEGMENT_ON)
      digitalWrite(segC, SEGMENT_ON)
      digitalWrite(segD, SEGMENT_ON)
      digitalWrite(segE, SEGMENT_ON)
      digitalWrite(segF, SEGMENT_ON)
      digitalWrite(segG, SEGMENT_ON)
      digitalWrite(DP, SEGMENT_OFF)

    elif numberToDisplay=='9':
      digitalWrite(segA, SEGMENT_ON)
      digitalWrite(segB, SEGMENT_ON)
      digitalWrite(segC, SEGMENT_ON)
      digitalWrite(segD, SEGMENT_ON)
      digitalWrite(segE, SEGMENT_OFF)
      digitalWrite(segF, SEGMENT_ON)
      digitalWrite(segG, SEGMENT_ON)
      digitalWrite(DP, SEGMENT_OFF)

    elif numberToDisplay=='10':
      digitalWrite(segA, SEGMENT_OFF)
      digitalWrite(segB, SEGMENT_OFF)
      digitalWrite(segC, SEGMENT_OFF)
      digitalWrite(segD, SEGMENT_OFF)
      digitalWrite(segE, SEGMENT_OFF)
      digitalWrite(segF, SEGMENT_OFF)
      digitalWrite(segG, SEGMENT_OFF)
      digitalWrite(DP, SEGMENT_OFF)

    elif numberToDisplay=='.':
      digitalWrite(segA, SEGMENT_OFF)
      digitalWrite(segB, SEGMENT_OFF)
      digitalWrite(segC, SEGMENT_OFF)
      digitalWrite(segD, SEGMENT_OFF)
      digitalWrite(segE, SEGMENT_OFF)
      digitalWrite(segF, SEGMENT_OFF)
      digitalWrite(segG, SEGMENT_OFF)
      digitalWrite(DP, SEGMENT_ON)


while true:
	displayString('12.34')
