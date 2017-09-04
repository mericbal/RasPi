import RPi.GPIO as GPIO
import time

from twilio.rest import Client
from credentials import sid, token, meric, nil,  my_twilio

client = Client(sid, token)
warning = 'Door has opened!'

GPIO.setmode(GPIO.BOARD)

red = 11
green = 13
blue = 15

GPIO.setup(red, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)
GPIO.setup(blue, GPIO.OUT)

def sensor(pin):
	reading = 0
	GPIO.setup(pin, GPIO.OUT)
	GPIO.output(pin, GPIO.LOW)
	time.sleep(0.7)
	
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
			GPIO.output(blue, True)
			time.sleep(0.2)
			GPIO.output(blue, False)

		if sensor(7) < 130:
			GPIO.output(green, GPIO.HIGH)
			time.sleep(2)
			message = client.messages.create(to=meric,
							from_=my_twilio,
							body=warning)
			print 'Message sent to %r !' % meric
			message2 = client.messages.create(to=nil,
							from_=my_twilio,
							body=warning)
			print 'Message sent to %r !' % nil
			print 'Returning to reading !'
			GPIO.output(green, GPIO.LOW)

		else:
			print 'Detection stopped ! Returning to reading !'


GPIO.cleanup()
