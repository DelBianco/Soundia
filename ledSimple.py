import RPi.GPIO as GPIO
import time
import math 

GPIO.setmode(GPIO.BCM)

pin1 = 17
pin2 = 27
pin3 = 22

GPIO.setwarnings(False)
GPIO.setup(pin1, GPIO.OUT)
GPIO.setup(pin2, GPIO.OUT)
GPIO.setup(pin3, GPIO.OUT)

RED = GPIO.PWM(pin1, 100)
GREEN = GPIO.PWM(pin2, 100)
BLUE = GPIO.PWM(pin3, 100)
RED.start(50)
BLUE.start(50)
GREEN.start(50)


def setRGB(red, green, blue):
	RED.ChangeDutyCycle(red)
	BLUE.ChangeDutyCycle(blue)
	GREEN.ChangeDutyCycle(green)

def cicleValue(Angle, Max = 100):
	return Max * pow(math.sin(Angle * math.pi / (2 * Max) ), 2)

cicle = 100
print "Loading ..."
while True:
	for i in range(cicle):
		setRGB(cicleValue(cicle - i), cicleValue(i) , 0)
		time.sleep(0.003)
	for i in range(cicle):
		setRGB(0,cicleValue(cicle - i), cicleValue(i))
		time.sleep(0.003)
	for i in range(cicle):
		setRGB(cicleValue(i), 0 , cicleValue(cicle - i))
		time.sleep(0.003)
