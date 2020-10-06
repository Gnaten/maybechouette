import RPi.GPIO as GPIO
import time
import random

LED = random.randint(11, 16)
thyme = 10

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(LED, GPIO.OUT)
    GPIO.output(LED, GPIO.LOW)
    if LED == 14:
        LED = random.randint(11, 16)
        setup()
    else:
        print('GPIO Pin ID: %d'%LED)
        countdown()

def countdown():
    global thyme
    print('Begin Wiring!')
    time.sleep(1)
    while thyme >= 0:
        print('Seconds Remaining: %d'%thyme)
        time.sleep(1)
        thyme = thyme - 1
    else:
        print('Initiating Protocol...')
        time.sleep(2.5)
        loop()

def loop():
    while True:
        GPIO.output(LED, GPIO.LOW)
        time.sleep(1)
        GPIO.output(LED, GPIO.HIGH)
        time.sleep(1)

def destroy():
    GPIO.cleanup()

if __name__ == '__main__':      #Checks if this module is running or being imported
    print('Initiating Python Executable...')
    setup()
    try:                        #Basically saying: Do 'this' until 'something' happens
        countdown()
    except KeyboardInterrupt:   #Line statement is the 'something'
        destroy()