#!/usr/bin/env python

import time
import RPi.GPIO as GPIO
from apns import APNs, Payload, PayloadAlert

motion_pin = 18

GPIO.setwarnings(False) #allows two scripts to access the same GPIO pin
GPIO.setmode(GPIO.BCM)
GPIO.setup(motion_pin, GPIO.OUT)

GPIO.output(motion_pin, GPIO.HIGH)
