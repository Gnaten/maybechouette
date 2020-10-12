#Goal: Create a script that move LED block in a wave, but YOLO-plz-dont-short style!
import RPi.GPIO as GPIO
import time

led = ["7", "11", "12", "13", "15", "38", "16", "40", "18", "22"]		#If using lists, make sure the numbers are in quotations

def setup():
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(7, GPIO.OUT)		#Setting up pins only for providing power
	GPIO.setup(11, GPIO.OUT)
	GPIO.setup(12, GPIO.OUT)
	GPIO.setup(13, GPIO.OUT)
	GPIO.setup(15, GPIO.OUT)
	GPIO.setup(38, GPIO.OUT)
	GPIO.setup(16, GPIO.OUT)
	GPIO.setup(40, GPIO.OUTPUT)
	GPIO.setup(18, GPIO.OUT)
	GPIO.setup(22, GPIO.OUT)
	GPIO.output(7, 0)			#Pins 7, 11, 12, and 13 are set to GPIO.LOW in output
	GPIO.output(11, 0)
	GPIO.output(12, 0)
	GPIO.output(13, 0)
	GPIO.output(15, 0)
	GPIO.output(38, 0)
	GPIO.output(16, 0)
	GPIO.output(40, 0)
	GPIO.output(18, 0)
	GPIO.output(22, 0)
	print('Setup Complete')
	time.sleep(1)

def loop():
	 while True:
	 	GPIO.output(led[0], 1)
	 	time.sleep(0.1)
	 	GPIO.output(led[0], 0)

	 	GPIO.output(led[1], 1)
	 	time.sleep(0.1)
	 	GPIO.output(led[1], 0)

	 	GPIO.output(led[2], 1)
	 	time.sleep(0.1)
	 	GPIO.output(led[2], 0)

	 	GPIO.output(led[3], 1)
	 	time.sleep(0.1)
	 	GPIO.output(led[3], 0)

			
			


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
