import RPi.GPIO as GPIO

LED = 7		#Replace number with desired PINOUT #

def setup():
   GPIO.setmode(GPIO.BOARD)
   GPIO.setup(LED, GPIO.OUT)
   GPIO.output(LED, GPIO.LOW)

def destroy():
	GPIO.cleanup()

if __name__ == '__main__':
   setup()
   destroy()
   print('GPIO.cleanup() Complete...')
