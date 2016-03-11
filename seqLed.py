import RPi.GPIO as gpio
import time, os, sys

gpio.setmode(gpio.BOARD)
gpio.setup(12, gpio.IN, pull_up_down=gpio.PUD_UP)   # Sets up button pin

R = 11
G = 13 #Pin numbers
B = 15
lights = [R,G,B]

for pin in lights:
    gpio.setup(pin, gpio.OUT) # Calls all pins in array sequentially so they are all out

ColourMode = ["Off", "White", "Red", "Green", "Blue"] # List of strings in array
Mode = 0

r = gpio.PWM(R,100) # sets pin and its max pwm
r.start(0)          # starts pwm
g = gpio.PWM(G,100)
g.start(0)
b = gpio.PWM(B,100)
b.start(0)

while True: # Loop
    changeColourMode = gpio.input(12)   # Checks button state
    if changeColourMode == False:   # If it was pressed:
        Mode = (Mode + 1) # Adds 1 to counter which changes what strings are printed next button change
        if Mode > 4: # If the end colour is reached it resets
            Mode = 0
        print ("Current Mode is: " + ColourMode[Mode]) # Prints change
        time.sleep(0.2)
    else:
        #print ("Current mode is: " + ColourMode[Mode])
        time.sleep(0.2) # Does nothing and repeats loop

    if Mode == 0:
        #print('OFF')
        r.ChangeDutyCycle(0)
        g.ChangeDutyCycle(0) #Off
        b.ChangeDutyCycle(0)        # Change PWM value from 0/100 to set how much power output to pin
    elif Mode == 1:
        #print('WHITE')
        r.ChangeDutyCycle(100)
        g.ChangeDutyCycle(60) #White
        b.ChangeDutyCycle(60)
    elif Mode == 2:
        #print('RED')
        r.ChangeDutyCycle(0)
        g.ChangeDutyCycle(0) #Red
        b.ChangeDutyCycle(0)
        r.ChangeDutyCycle(100)
    elif Mode == 3:
        #print('GREEN')
        r.ChangeDutyCycle(0) #Green
        g.ChangeDutyCycle(100)
    elif Mode == 4:
        #print('BLUE')
        g.ChangeDutyCycle(0) #Blue
        b.ChangeDutyCycle(100)

gpio.cleanup()
sys.exit()
