import RPi.GPIO as GPIO
import time

from twilio.rest import Client
from credentials import sid, token, meric, my_twilio

client = Client(sid, token)
warning = 'Door has opened!'

GPIO.setmode(GPIO.BOARD)

red = 11
green = 13

GPIO.setup(red, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)

def sensor(pin):
	reading = 0
	GPIO.setup(pin, GPIO.OUT)
	GPIO.output(pin, GPIO.LOW)
	time.sleep(1)
	
	GPIO.setup(pin, GPIO.IN)
	
	while (GPIO.input(pin) == GPIO.LOW):
		reading += 1
	return reading

while True:
	print sensor(7)
	
	if sensor(7) < 130:
		print 'Movement detected !'
		for i in range(10):
			GPIO.output(red, True)
			time.sleep(0.2)
			GPIO.output(red, False)
			GPIO.output(green, True)
			time.sleep(0.2)
			GPIO.output(green, False)
			
		if sensor(7) < 130:
#			message = client.messages.create(to=meric,
#							from_=my_twilio,
#							body=warning)
			print 'Message sent to %r !' % meric
			print 'Returning to reading !'

		else:
			print 'Returning to reading !'


GPIO.cleanup()
