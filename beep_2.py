#Goal: Create a script that move LED block in a wave, but YOLO-plz-dont-short style!
import RPi.GPIO as GPIO
import time

def setup():
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(7, GPIO.OUT)
	GPIO.setup(11, GPIO.OUT)
	GPIO.setup(12, GPIO.OUT)
	GPIO.setup(13, GPIO.OUT)
	GPIO.output(7, 0)		#Pins 7, 11, 12, and 13 are set to GPIO.LOW in output
	GPIO.output(11, 0)
	GPIO.output(12, 0)
	GPIO.output(13, 0)
	print('Setup Complete')
	time.sleep(1)

def loop():
	while True:
		GPIO.output(7, 1)
		time.sleep(0.1)
		GPIO.output(7, 0)

		GPIO.output(11, 1)
		time.sleep(0.1)
		GPIO.output(11, 0)

		GPIO.output(12, 1)
		time.sleep(0.1)
		GPIO.output(12, 0)

		GPIO.output(13, 1)
		time.sleep(0.1)
		GPIO.output(13, 0)

def destroy():
	GPIO.cleanup()

if __name__ == '__main__':
	print('\nSetup Sequencing...\n')
	time.sleep(1)
	setup()
	try:
		loop()
	except KeyboardInterrupt:
		destroy()
