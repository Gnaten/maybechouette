import RPi.GPIO as GPIO
import random
import time

led = 12

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(led, GPIO.OUT)
    GPIO.output(led, GPIO.LOW) #set pin12 to low power so the led wont turned on when the script starts
    print("using pin%d"%led)

def loop():
    while True:
        GPIO.output(led, GPIO.HIGH)
        print('LED turned on')
        time.sleep(1)
        GPIO.output(led, GPIO.LOW)
        print('LED turned off')
        time.sleep(1)

def destroy():
    GPIO.cleanup() #unbind defined GPIO pins

if __name__ == '__main__':
    print('Initiating Python Executable...')
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()