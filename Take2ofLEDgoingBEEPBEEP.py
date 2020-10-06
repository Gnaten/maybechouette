import RPi.GPIO as GPIO
import time
import random
#REEEEEEEEEEEEEEEEEEEEEEEEEEE is all I can say atm

ledPin = random.randint(11, 16)    #using ledPinPin is a unique var in that you won't need to reference it in a function
thyme = 10

def setup():
    # global ledPin
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(ledPin, GPIO.OUT)
    GPIO.output(ledPin, GPIO.LOW)
    if ledPin == 14:
        ledPin = random.randint(11, 16)
        setup()
    else:
        print('\nGPIO Pin ID: %d'%ledPin)
        countdown()

def countdown():
    global thyme
    print('\nBegin Wiring!')
    time.sleep(1)
    while thyme >= 0:
        print('Seconds Remaining: %d'%thyme)
        time.sleep(1)
        thyme = thyme - 1
    else:
        print('Initiating Protocol...')
        time.sleep(2.5)
        print('Ctrl + C to Disable')
        loop()

def loop():
    while True:
        GPIO.output(ledPin, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(ledPin, GPIO.LOW)
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