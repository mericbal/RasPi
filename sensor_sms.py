import RPi.GPIO as GPIO, time
from twilio.rest import Client
from credentials import sid, token, my_cell, my_twilio

client = Client(sid, token)
msg = 'Movement in the room !'

GPIO.cleanup()

debug = 1
GPIO.setmode(GPIO.BOARD)

red = 11
green = 13

GPIO.setup(red, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)


def rc_time(pin):
        reading = 0
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, GPIO.LOW)
        time.sleep(0.1)

        GPIO.setup(pin, GPIO.IN)

        while (GPIO.input(pin) == GPIO.LOW):
                reading += 1
        return reading

while True:
        print rc_time(7)

        if rc_time(7) < 280:
                GPIO.output(red, True)
                GPIO.output(green, False)
        elif rc_time(7) > 281:
                GPIO.output(red, False)
                GPIO.output(green, True)
		#message = client.messages.create(to=my_cell,
		#				from_=my_twilio,
		#				body=msg)
		print 'Message sent !'
        else:
                GPIO.output(red, False)
                GPIO.output(green, False)


GPIO.cleanup()
