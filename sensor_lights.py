import RPi.GPIO as GPIO, time

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
	
	if rc_time(7) < 1000:
		GPIO.output(red, True)
		GPIO.output(green, False)
	elif rc_time(7) > 1000:
		GPIO.output(red, False)
		GPIO.output(green, True)
	else:
		GPIO.output(red, False)
		GPIO.output(green, False)
