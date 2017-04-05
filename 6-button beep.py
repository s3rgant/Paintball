#Import Libraries
import os
import time
import RPi.GPIO as GPIO

#set the GPIO pin naming mode
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
PINBuzzer = 22 # Sets the buzzer pin 22

#Sets PINBuzzer as an output pin and initialise it to 'off'
GPIO.setup(PINBuzzer, GPIO.OUT)
GPIO.output(PINBuzzer, GPIO.LOW)

def dot(): # A single morse dot
    GPIO.output(PINBuzzer, GPIO.HIGH)
    time.sleep(0.1)
    GPIO.output(PINBuzzer, GPIO.LOW)
    time.sleep(0.1)

#Set pin 25 as an input pin
ButtonPin = 25
GPIO.setup(ButtonPin, GPIO.IN)

print("-------------")
print("Button + GPIO")
print("-------------")

print(GPIO.input(ButtonPin))

while True:
    if GPIO.input(ButtonPin) == False:
        print("button Pressed")
        dot()
        time.sleep(1)
    else:
        os.system('clear')
        print("Waiting for you to push the button")

    time.sleep(0.5)
