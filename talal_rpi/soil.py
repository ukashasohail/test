import time
import random
import RPi.GPIO as GPIO
import requests
import board
import busio

import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

def soil():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    i2c = busio.I2C(board.SCL, board.SDA)
    ads = ADS.ADS1115(i2c)
    chan = AnalogIn(ads, ADS.P0)
    chan2 = AnalogIn(ads, ADS.P1)
    chan3 = AnalogIn(ads, ADS.P2)


    while True:

        soil = (((chan.voltage + chan2.voltage + chan3.voltage)/3)*24.4140)

        time.sleep(2)
        print(soil)

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(11, GPIO.OUT)
        GPIO.output(11, GPIO.HIGH)
        time.sleep(3)
        GPIO.cleanup()
