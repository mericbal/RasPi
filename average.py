import RPi.GPIO as GPIO, time

GPIO.setmode(GPIO.BOARD)

pin = 7

red = 11
GPIO.setup(red, GPIO.OUT)

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
counter = 10

for i in range(counter):
	counter -= 1
	print 'running ... ' + str(counter) + ' ... ' 
#	print str(sensor(pin))
	GPIO.output(red, True)  
	total += sensor(pin)

print 'Average --> ' + str(total/10)

GPIO.cleanup()
