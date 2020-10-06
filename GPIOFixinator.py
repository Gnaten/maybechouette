import RPi.GPIO as GPIO

LED = 15		#Replace number with desired PINOUT #

def setup():
   GPIO.setmode(GPIO.BOARD)
   GPIO.setup(LED, GPIO.OUT)
   GPIO.output(LED, GPIO.LOW)

def destroy():
	GPIO.cleanup()

if __name__ == '__main__':
   setup()
