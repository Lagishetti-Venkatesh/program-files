#!/usr/bin/python
import RPi.GPIO as GPIO
import time
 
#GPIO SETUP
channel = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)
 
def callback(channel):
        if GPIO.input(channel):
                print("Water Detected!")
        else:
                print ("Water Detected!")
 

while True:
        time.sleep(1)
        print(GPIO.input(channel))

