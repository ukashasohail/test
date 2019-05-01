#importing rpi.gpio module
import RPi.GPIO as GPIO
import time #importing time module

#setting gpio to BCM
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#setting BCM pin 18 as output
GPIO.setup(18,GPIO.OUT)

#LED ON FOR 1 SEC
print ("LED on")
GPIO.output(18,GPIO.HIGH)

time.sleep(1)

#LED OFF FOR 1 SECOND
print ("LED off")
GPIO.output(18,GPIO.LOW)