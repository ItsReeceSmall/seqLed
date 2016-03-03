import RPi.GPIO as gpio
import time, os, sys

gpio.setmode(gpio.BOARD)
gpio.setup(12, gpio.IN, pull_up_down=gpio.PUD_UP)

R = 11
G = 13
B = 15
lights = [R,G,B]

for pin in lights:
    gpio.setup(pin, gpio.OUT)

ColourMode = ["w", "R", "G", "B", "Off"]
Mode = 0

while True:
    if gpio.input(12) == False:
        time.sleep(1)
        print('on')
        time.sleep(1)
    else:
        time.sleep(1)
        print('off')
        time.sleep(1)

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
        print('OFF')
    elif Mode == 1:)
        print('WHITE')
    elif Mode == 2:
        print('RED')
    elif Mode == 3:
        print('GREEN')
    elif Mode == 4:
        print('BLUE')

gpio.cleanup()
sys.exit()
