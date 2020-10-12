#Goal: Create a script that move LED block in a wave, but YOLO-plz-dont-short style!
import RPi.GPIO as GPIO
import time

led = [7, 11, 12, 13, 15, 38, 16, 40, 18, 22]		#If using lists, make sure the numbers are in quotations

def setup():
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(led, GPIO.OUT)		#Setting up pins only for providing power
	GPIO.output(led, 0)			#Pins 7, 11, 12, and 13 are set to GPIO.LOW in output
	print('Setup Complete')
	time.sleep(1)

def loop():
	 while True:
		 for pin in led:
			 GPIO.output(pin, 1)
			 time.sleep(0.1)
			 GPIO.output(pin, 0)
		for pin in led[::-1]:
			GPIO.output(pin, 1)
			time.sleep(0.1)
			GPIO.output(pin, 0)

# #Farewell light wave!
# 	 	GPIO.output(led[0], 1)
# 	 	time.sleep(0.1)
# 	 	GPIO.output(led[0], 0)

# 	 	GPIO.output(led[1], 1)
# 	 	time.sleep(0.1)
# 	 	GPIO.output(led[1], 0)

# 	 	GPIO.output(led[2], 1)
# 	 	time.sleep(0.1)
# 	 	GPIO.output(led[2], 0)

# 	 	GPIO.output(led[3], 1)
# 	 	time.sleep(0.1)
# 	 	GPIO.output(led[3], 0)

# 	 	GPIO.output(led[4], 1)
# 	 	time.sleep(0.1)
# 	 	GPIO.output(led[4], 0)

# 	 	GPIO.output(led[5], 1)
# 	 	time.sleep(0.1)
# 	 	GPIO.output(led[5], 0)

# 	 	GPIO.output(led[6], 1)
# 	 	time.sleep(0.1)
# 	 	GPIO.output(led[6], 0)

# 	 	GPIO.output(led[7], 1)
# 	 	time.sleep(0.1)
# 	 	GPIO.output(led[7], 0)

# 	 	GPIO.output(led[8], 1)
# 	 	time.sleep(0.1)
# 	 	GPIO.output(led[8], 0)

# 	 	GPIO.output(led[9], 1)
# 	 	time.sleep(0.1)
# 	 	GPIO.output(led[9], 0)

# #Bringing the light wave back home!

# 	 	GPIO.output(led[9], 1)
# 	 	time.sleep(0.1)
# 	 	GPIO.output(led[9], 0)

# 	 	GPIO.output(led[8], 1)
# 	 	time.sleep(0.1)
# 	 	GPIO.output(led[8], 0)

# 	 	GPIO.output(led[7], 1)
# 	 	time.sleep(0.1)
# 	 	GPIO.output(led[7], 0)

# 	 	GPIO.output(led[6], 1)
# 	 	time.sleep(0.1)
# 	 	GPIO.output(led[6], 0)

# 	 	GPIO.output(led[5], 1)
# 	 	time.sleep(0.1)
# 	 	GPIO.output(led[5], 0)

# 	 	GPIO.output(led[4], 1)
# 	 	time.sleep(0.1)
# 	 	GPIO.output(led[4], 0)

# 	 	GPIO.output(led[3], 1)
# 	 	time.sleep(0.1)
# 	 	GPIO.output(led[3], 0)

# 	 	GPIO.output(led[2], 1)
# 	 	time.sleep(0.1)
# 	 	GPIO.output(led[2], 0)

# 	 	GPIO.output(led[1], 1)
# 	 	time.sleep(0.1)
# 	 	GPIO.output(led[1], 0)

# 	 	GPIO.output(led[0], 1)
# 	 	time.sleep(0.1)
# 	 	GPIO.output(led[0], 0)


def destroy():
	GPIO.cleanup()

if __name__ == '__main__':
	print('\nSetup Sequencing...')
	time.sleep(1)
	setup()
	print('\nRunning...')
	try:
		loop()
	except KeyboardInterrupt:
		print(' --> Stopped')
		destroy()
