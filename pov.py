import sys, traceback
import RPi.GPIO as GPIO
import time, os
from scrollable_led import ScrollableLED

'''We are using the following 5 GPIO pins'''
__LED0 = 13
__LED1 = 19
__LED2 = 26
__LED3 = 21
__LED4 = 20

def to_screen(viewport):
  os.system("clear")
  print viewport[0], "\n", viewport[1], "\n", viewport[2], "\n", viewport[3], "\n", viewport[4]

def to_LED(viewport):
  GPIO.output(__LED0, viewport[0] == "#")
  GPIO.output(__LED1, viewport[1] == "#")
  GPIO.output(__LED2, viewport[2] == "#")
  GPIO.output(__LED3, viewport[3] == "#")
  GPIO.output(__LED4, viewport[4] == "#")

def test1():
  for _ in range(5): #blick LEDs 5 times
    for pin in [__LED0, __LED1, __LED2, __LED3, __LED4]:
      GPIO.output(pin,True)
      time.sleep(0.1) #blink for 0.1 second
      GPIO.output(pin,False)

def test2():
  led = ScrollableLED("happy mother's day")
  for viewport in led.viewport_generator(8):
    to_screen(viewport)
    time.sleep(0.2)

def test3():
  led = ScrollableLED("happy mother's day")
  for viewport1 in led.viewport_generator(8):
    to_screen(viewport1)
    to_LED(led.get_viewport(1))
    time.sleep(0.2)

try:
  GPIO.setmode(GPIO.BCM)
  GPIO.setwarnings(True)

  for pin in [__LED0, __LED1, __LED2, __LED3, __LED4]:
    GPIO.setup(pin,GPIO.OUT) # Set all the pins to OUTPUT

  options = {"1":test1, "2":test2, "3":test3}
  input = raw_input("Enter option (1, 2 or 3):")
  options[input]()

except KeyboardInterrupt:
  print "\n"

except:
  print "*** An exception may have occurred:"
  exc_type, exc_value, exc_traceback = sys.exc_info()
  traceback.print_exc()

finally:
  GPIO.cleanup()
