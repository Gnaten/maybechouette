import RPi.GPIO as GPIO
import time, random

pins = [7, 11, 12, 13, 15, 16, 18, 22, 38, 40]
  
def setup():
  print('Setting up pin #%d'%pins)
  GPIO.setmode(GPIO.BOARD)
  GPIO.setup(pins, GPIO.OUT)
  GPIO.OUTPUT(pins, 0)        #1 = set initial voltage to LOW
  print('\nSetup Complete')
  time.sleep(2)

def loop():
  while True:
    for i in pins:
      GPIO.OUTPUT(pins, 1)
      time.sleep(0.1)
      GPIO.OUTPUT(pins, 0)
      time.sleep(0.1)
        
    for i in pins[::-1]:
      GPIO.OUTPUT(pins, 1)
      time.sleep(0,1)
      GPIO.OUTPUT(pins, 0)
      time.sleep(0.1)
        
def destroy():
  GPIO.cleanup()
    
if __name__ == '__main__':
  setup()
  try:
    loop()
  except KeyboardInterrupt:
    destroy()
