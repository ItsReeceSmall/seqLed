import RPi.GPIO as gpio
import time, os, sys

gpio.setmode(gpio.BOARD)
gpio.setup(12, gpio.IN, pull_up_down=gpio.PUD_UP)

R = 11
G = 13
B = 15
lights = [R,G,B]
count = 0

for pin in lights:
    gpio.setup(pin, gpio.OUT)

ColourMode = ["Off", "w", "R", "G", "B"]
Mode = 0

r = gpio.PWM(R,100)
r.start(0)
g = gpio.PWM(G,100)
g.start(0)
b = gpio.PWM(B,100)
b.start(0)

while True:
    changeColourMode = gpio.input(12)
    if changeColourMode == False:
        Mode = (Mode + 1)
        if Mode > 4:
            Mode = 0
        print ("Current Mode is: " + ColourMode[Mode])
        time.sleep(0.05)
    else:
        #print ("Current mode is: " + ColourMode[Mode])
        time.sleep(0.05)

    if Mode == 0:
        print('OFF')
        r.ChangeDutyCycle(0)
        g.ChangeDutyCycle(0)
        b.ChangeDutyCycle(0)
    elif Mode == 1:
        print('WHITE')
        r.ChangeDutyCycle(100)
        g.ChangeDutyCycle(60)
        b.ChangeDutyCycle(60)
    elif Mode == 2:
        print('RED')
        r.ChangeDutyCycle(0)
        g.ChangeDutyCycle(0)
        b.ChangeDutyCycle(0)
        r.ChangeDutyCycle(100)
    elif Mode == 3:
        print('GREEN')
        r.ChangeDutyCycle(0)
        g.ChangeDutyCycle(100)
    elif Mode == 4:
        print('BLUE')
        g.ChangeDutyCycle(0)
        b.ChangeDutyCycle(100)

gpio.cleanup()
sys.exit()
