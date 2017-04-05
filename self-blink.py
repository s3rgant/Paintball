#Import Libraries
import time
import RPi.GPIO as GPIO

#Set the GPIO pin naming mode
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#Set Pins 18, 34 and 24 to be output
GPIO.setup(18, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)

#Turn LEDs on
GPIO.output(18, GPIO.HIGH)
GPIO.output(23, GPIO.HIGH)
GPIO.output(24, GPIO.HIGH)

time.sleep(1)

#Turn LEDs off
GPIO.output(18, GPIO.LOW)
GPIO.output(23, GPIO.LOW)
GPIO.output(24, GPIO.LOW)

time.sleep(1)

#Turn LEDs on
GPIO.output(18, GPIO.HIGH)
GPIO.output(23, GPIO.HIGH)
GPIO.output(24, GPIO.HIGH)

time.sleep(1)

#Turn LEDs off
GPIO.output(18, GPIO.LOW)
GPIO.output(23, GPIO.LOW)
GPIO.output(24, GPIO.LOW)

#Clean up the GPIO Pins
GPIO.cleanup()
