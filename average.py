# takes one arg to run
# Ex 'python average.py 30'

from sys import argv
import RPi.GPIO as GPIO, time

script,timer = argv
print 'Sensor reading is going to take %r' % timer + ' seconds ...'

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
counter = int(timer)

for i in range(counter):
	counter -= 1
	print 'running ... ' + str(counter) + ' ... ' 
#	print str(sensor(pin))
	GPIO.output(red, True)  
	total += sensor(pin)


print 'Average for %r seconds --> ' % timer  + str(total/int(timer))

GPIO.cleanup()
