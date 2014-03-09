#!/usr/bin/env python

import time
import RPi.GPIO as GPIO
from apns import APNs, Payload, PayloadAlert

button_pin = 25
motion_input_pin = 24
motion_output_pin = 23
motion_trigger_pin = 18

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(button_pin, GPIO.IN)
GPIO.setup(motion_input_pin, GPIO.IN)
GPIO.setup(motion_output_pin, GPIO.OUT)
GPIO.setup(motion_trigger_pin, GPIO.OUT)

apns = APNs(use_sandbox=True, cert_file='/home/pi/eyedoor/keys/apns.pem', key_file='/home/pi/eyedoor/keys/key-noenc.pem')
device_token = 'c6776af9bf6d9fab0c14f1e7f30115706ffeaac99ae4df29a9e1fbef87b87b01'

button_press_alert = PayloadAlert("Doorbell pressed", action_loc_key="View eyeDoor")
button_press_payload = Payload(alert=button_press_alert, sound="doorbell.wav", custom={'type': 'button'})

motion_detect_alert = PayloadAlert("Motion detected", action_loc_key="View eyeDoor")
motion_detect_payload = Payload(alert=motion_detect_alert, sound="alert.caf", custom={'type': 'motion'})

previous_button_value = False
previous_motion_value = False

GPIO.output(motion_trigger_pin, GPIO.LOW)

while True:
	new_button_value = GPIO.input(button_pin)
	if ((not previous_button_value) and new_button_value):
		print("Doorbell pressed")
		apns.gateway_server.send_notification(device_token, button_press_payload)
		
	new_motion_value = GPIO.input(motion_input_pin)
	if (previous_motion_value != new_motion_value):
		if new_motion_value:
			print("Motion detected")
			apns.gateway_server.send_notification(device_token, motion_detect_payload)
		else:
			print("Motion stopped")
			
		GPIO.output(motion_output_pin, new_motion_value)

	previous_motion_value = new_motion_value
	previous_button_value = new_button_value
	time.sleep(0.05)
