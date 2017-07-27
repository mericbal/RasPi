import RPi.GPIO as GPIO, time

GPIO.setmode(GPIO.BOARD)

pin = 7

def sensor(pin):
	reading = 0
	
	GPIO.setup(pin, GPIO.OUT)
	GPIO.output(pin, GPIO.LOW)
	time.sleep(1)

	GPIO.setup(pin, GPIO.IN)

	while (GPIO.input(pin) == GPIO.LOW):
		reading += 1
	return reading

total = 0
counter = 60

for i in range(60):
	counter -= 1
	print 'running ... ' + str(counter)  
	total += sensor(pin)

print total / 60

GPIO.cleanup()
