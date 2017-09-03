# needs an agrument to run
# Ex 'python sensor.py 0.5' or 0.1 or 2 etc   

from sys import argv
import RPi.GPIO as GPIO, time

script,timer = argv
print 'Reading is starting for every %r' % timer + ' seconds.'

GPIO.setmode(GPIO.BOARD)

pin = 7

def rc_time(pin):
        count = 0

        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, GPIO.LOW)
        time.sleep(float(timer))

        GPIO.setup(pin, GPIO.IN)

        while (GPIO.input(pin) == GPIO.LOW):
                count  += 1

        return count

try:
        while True:
                print rc_time(pin)
except KeyboardInterrupt:
        pass
finally:
        GPIO.cleanup()
