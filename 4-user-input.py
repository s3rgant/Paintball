#Import Libraries
import os
import time
import RPi.GPIO as GPIO

#Set the GPIO pin naming mode
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#set up variables to store the pin numbers
LEDRed = 18
LEDYellow = 23
LEDGreen = 24

#set the LED pins to output
GPIO.setup(LEDRed, GPIO.OUT)
GPIO.setup(LEDYellow, GPIO.OUT)
GPIO.setup(LEDGreen, GPIO.OUT)

os.system('clear')

print("Which LED would you link to blink")
print("1: Red?")
print("2 Yellow?")
print("3 Green?")

#Prints prompts to the screen and waits for input from the user
led_choice = input("Choose your option: ")
count = input("How many times would you like to blink?:")

#Convert User input from string(text) to integer
led_choice = int(led_choice)
count = int(count)

#Set the LEDChoice variable depending on the LED choice
if led_choice == 1:
    print("You Picked the Red LED")
    LEDChoice = LEDRed
if led_choice == 2:
    print("You Picked the Yellow LED")
    LEDChoice = LEDYellow
if led_choice == 3:
    print("You Picked the Green LED")
    LEDChoice = LEDGreen
#If we have chosen a valid choice, flash the LED
if LEDChoice>0:
    while count > 0:
        GPIO.output(LEDChoice, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(LEDChoice, GPIO.LOW)
        time.sleep(1)
        count = count - 1

GPIO.cleanup()


