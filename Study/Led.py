import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(23,GPIO.OUT)
GPIO.setup(24,GPIO.OUT)
GPIO.setup(25,GPIO.OUT)
GPIO.setup(1,GPIO.OUT)
try:
	while 1:
    	GPIO.output(23,GPIO.HIGH)
        GPIO.output(24,GPIO.HIGH)
        GPIO.output(25,GPIO.HIGH)
        GPIO.output(1,GPIO.HIGH)
        time.sleep(1.0)
        GPIO.output(23,GPIO.LOW)
        GPIO.output(24,GPIO.LOW)
        GPIO.output(25,GPIO.LOW)
        GPIO.output(1,GPIO.LOW)
        time.sleep(1.0)
except KeyboardInterrupt:
	pass
GPIO.cleanup()
