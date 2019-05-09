from time import sleep
import os
import RPi.GPIO as GPIO

def rain():

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(23, GPIO.IN)
    state = GPIO.input(23)
    servoPIN = 17
    GPIO.setup(servoPIN, GPIO.OUT)

    p = GPIO.PWM(servoPIN, 50)  # GPIO 17 for PWM with 50Hz
    p.start(0)  # Initialization

    if (state == 0):
        print("Water detected!")
        try:
            while True:
                p.ChangeDutyCycle(5)
                time.sleep(0.5)

        except KeyboardInterrupt:

            p.stop()
            GPIO.cleanup()
    else:
        print("Water not detected")
