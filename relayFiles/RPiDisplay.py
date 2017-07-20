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
	DISPLAY_BRIGHTNESS = 0.00001
	DIGIT_ON = GPIO.HIGH
        DIGIT_OFF = GPIO.LOW
    
        for i in range(0,5):
                if i==0:
                        GPIO.output(digit1,DIGIT_ON)
                elif i==1:
                        GPIO.output(digit2, DIGIT_ON)
                elif i==2:
                    GPIO.output(digit2, DIGIT_ON)
                elif i==3:
                    GPIO.output(digit3, DIGIT_ON)
                elif i==4:
                    GPIO.output(digit4, DIGIT_ON)

                lightNumber(toDisplay[i])
                sleep(DISPLAY_BRIGHTNESS)
                lightNumber('10')

                GPIO.output(digit1, DIGIT_OFF)
                GPIO.output(digit2, DIGIT_OFF)
                GPIO.output(digit3, DIGIT_OFF)
                GPIO.output(digit4, DIGIT_OFF)
                sleep(0.005)

def lightNumber(numberToDisplay):
    SEGMENT_ON = GPIO.LOW
    SEGMENT_OFF = GPIO.HIGH

    if numberToDisplay=='0':
      GPIO.output(segA, SEGMENT_ON)
      GPIO.output(segB, SEGMENT_ON)
      GPIO.output(segC, SEGMENT_ON)
      GPIO.output(segD, SEGMENT_ON)
      GPIO.output(segE, SEGMENT_ON)
      GPIO.output(segF, SEGMENT_ON)
      GPIO.output(segG, SEGMENT_OFF)
      GPIO.output(DP, SEGMENT_OFF)

    elif numberToDisplay=='1':
      GPIO.output(segA, SEGMENT_OFF)
      GPIO.output(segB, SEGMENT_ON)
      GPIO.output(segC, SEGMENT_ON)
      GPIO.output(segD, SEGMENT_OFF)
      GPIO.output(segE, SEGMENT_OFF)
      GPIO.output(segF, SEGMENT_OFF)
      GPIO.output(segG, SEGMENT_OFF)
      GPIO.output(DP, SEGMENT_OFF)

    elif numberToDisplay=='2':
      GPIO.output(segA, SEGMENT_ON)
      GPIO.output(segB, SEGMENT_ON)
      GPIO.output(segC, SEGMENT_OFF)
      GPIO.output(segD, SEGMENT_ON)
      GPIO.output(segE, SEGMENT_ON)
      GPIO.output(segF, SEGMENT_OFF)
      GPIO.output(segG, SEGMENT_ON)
      GPIO.output(DP, SEGMENT_OFF)

    elif numberToDisplay=='3':
      GPIO.output(segA, SEGMENT_ON)
      GPIO.output(segB, SEGMENT_ON)
      GPIO.output(segC, SEGMENT_ON)
      GPIO.output(segD, SEGMENT_ON)
      GPIO.output(segE, SEGMENT_OFF)
      GPIO.output(segF, SEGMENT_OFF)
      GPIO.output(segG, SEGMENT_ON)
      GPIO.output(DP, SEGMENT_OFF)

    elif numberToDisplay=='4':
      GPIO.output(segA, SEGMENT_OFF)
      GPIO.output(segB, SEGMENT_ON)
      GPIO.output(segC, SEGMENT_ON)
      GPIO.output(segD, SEGMENT_OFF)
      GPIO.output(segE, SEGMENT_OFF)
      GPIO.output(segF, SEGMENT_ON)
      GPIO.output(segG, SEGMENT_ON)
      GPIO.output(DP, SEGMENT_OFF)

    elif numberToDisplay=='5':
      GPIO.output(segA, SEGMENT_ON)
      GPIO.output(segB, SEGMENT_OFF)
      GPIO.output(segC, SEGMENT_ON)
      GPIO.output(segD, SEGMENT_ON)
      GPIO.output(segE, SEGMENT_OFF)
      GPIO.output(segF, SEGMENT_ON)
      GPIO.output(segG, SEGMENT_ON)
      GPIO.output(DP, SEGMENT_OFF)

    elif numberToDisplay=='6':
      GPIO.output(segA, SEGMENT_ON)
      GPIO.output(segB, SEGMENT_OFF)
      GPIO.output(segC, SEGMENT_ON)
      GPIO.output(segD, SEGMENT_ON)
      GPIO.output(segE, SEGMENT_ON)
      GPIO.output(segF, SEGMENT_ON)
      GPIO.output(segG, SEGMENT_ON)
      GPIO.output(DP, SEGMENT_OFF)

    elif numberToDisplay=='7':
      GPIO.output(segA, SEGMENT_ON)
      GPIO.output(segB, SEGMENT_ON)
      GPIO.output(segC, SEGMENT_ON)
      GPIO.output(segD, SEGMENT_OFF)
      GPIO.output(segE, SEGMENT_OFF)
      GPIO.output(segF, SEGMENT_OFF)
      GPIO.output(segG, SEGMENT_OFF)
      GPIO.output(DP, SEGMENT_OFF)

    elif numberToDisplay=='8':
      GPIO.output(segA, SEGMENT_ON)
      GPIO.output(segB, SEGMENT_ON)
      GPIO.output(segC, SEGMENT_ON)
      GPIO.output(segD, SEGMENT_ON)
      GPIO.output(segE, SEGMENT_ON)
      GPIO.output(segF, SEGMENT_ON)
      GPIO.output(segG, SEGMENT_ON)
      GPIO.output(DP, SEGMENT_OFF)

    elif numberToDisplay=='9':
      GPIO.output(segA, SEGMENT_ON)
      GPIO.output(segB, SEGMENT_ON)
      GPIO.output(segC, SEGMENT_ON)
      GPIO.output(segD, SEGMENT_ON)
      GPIO.output(segE, SEGMENT_OFF)
      GPIO.output(segF, SEGMENT_ON)
      GPIO.output(segG, SEGMENT_ON)
      GPIO.output(DP, SEGMENT_OFF)

    elif numberToDisplay=='10':
      GPIO.output(segA, SEGMENT_OFF)
      GPIO.output(segB, SEGMENT_OFF)
      GPIO.output(segC, SEGMENT_OFF)
      GPIO.output(segD, SEGMENT_OFF)
      GPIO.output(segE, SEGMENT_OFF)
      GPIO.output(segF, SEGMENT_OFF)
      GPIO.output(segG, SEGMENT_OFF)
      GPIO.output(DP, SEGMENT_OFF)

    elif numberToDisplay=='.':
      GPIO.output(segA, SEGMENT_OFF)
      GPIO.output(segB, SEGMENT_OFF)
      GPIO.output(segC, SEGMENT_OFF)
      GPIO.output(segD, SEGMENT_OFF)
      GPIO.output(segE, SEGMENT_OFF)
      GPIO.output(segF, SEGMENT_OFF)
      GPIO.output(segG, SEGMENT_OFF)
      GPIO.output(DP, SEGMENT_ON)

counter = 0
toDisplay = 11.11
while counter < 100:
        thing = '%.2f' % toDisplay
	displayString(thing)
	counter = counter + 1
	toDisplay = toDisplay + 0.01
	print toDisplay

GPIO.cleanup()
