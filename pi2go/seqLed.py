import RPi.GPIO as GPIO
import pi2go
import time, os, sys

pi2go.init()

ColourMode = ["w", "R", "G", "B", "Off"]
Mode = 0
pi2go.setAllLEDs(0, 0, 0)

while True:
    if pi2go.getSwitch() == True:
        print('on')
    else:
        print('off')

while True:
    changeColourMode = pi2go.getSwitch()
    if changeColourMode == True:
        Mode = (Mode + 1)
        if Mode > 4:
            Mode = 0
        print ("Current Mode is: " + ColourMode[Mode])
        time.sleep(1)
    else:
        print ("Current mode is: " + ColourMode[Mode])
        time.sleep(1)

    if Mode == 0:
        pi2go.setLED(0, 0, 0, 0)
        pi2go.setLED(1, 0, 0, 0)
        pi2go.setLED(2, 0, 0, 0)
        pi2go.setLED(3, 0, 0, 0)
        print('OFF')
    elif Mode == 1:
        pi2go.setLED(0, 4095, 4095, 4095)
        pi2go.setLED(1, 4095, 4095, 4095)
        pi2go.setLED(2, 4095, 4095, 4095)
        pi2go.setLED(3, 4095, 4095, 4095)
        print('WHITE')
    elif Mode == 2:
        pi2go.setLED(0, 4095, 0, 0)
        pi2go.setLED(1, 4095, 0, 0)
        pi2go.setLED(2, 4095, 0, 0)
        pi2go.setLED(3, 4095, 0, 0)
        print('RED')
    elif Mode == 3:
        pi2go.setLED(0, 0, 4095, 0)
        pi2go.setLED(1, 0, 4095, 0)
        pi2go.setLED(2, 0, 4095, 0)
        pi2go.setLED(3, 0, 4095, 0)
        print('GREEN')
    elif Mode == 4:
        pi2go.setLED(0, 0, 0, 4095)
        pi2go.setLED(1, 0, 0, 4095)
        pi2go.setLED(2, 0, 0, 4095)
        pi2go.setLED(3, 0, 0, 4095)
        print('BLUE')

GPIO.cleanup()
sys.exit()