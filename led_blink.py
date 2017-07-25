import RPi.GPIO as GPIO
import time

GPIO.cleanup()
GPIO.setmode(GPIO.BOARD)

GPIO.setup(12,GPIO.OUT)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)

for i in range(20):
        GPIO.output(12, GPIO.HIGH)
        time.sleep(0.2)
        GPIO.output(12, GPIO.LOW)
	GPIO.output(11, GPIO.HIGH)
        time.sleep(0.2)
	GPIO.output(11, GPIO.LOW)
	GPIO.output(13, GPIO.HIGH)
	time.sleep(0.2)
	GPIO.output(13, GPIO.LOW)

GPIO.cleanup()

