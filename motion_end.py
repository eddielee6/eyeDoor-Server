#!/usr/bin/env python

import time
import RPi.GPIO as GPIO
from apns import APNs, Payload, PayloadAlert

motion_pin = 18
motion_output_pin = 23

GPIO.setwarnings(False) #allows two scripts to access the same GPIO pin
GPIO.setmode(GPIO.BCM)
GPIO.setup(motion_pin, GPIO.OUT)
GPIO.setup(motion_output_pin, GPIO.OUT)

GPIO.output(motion_pin, GPIO.LOW)
GPIO.output(motion_output_pin, GPIO.LOW)