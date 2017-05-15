import sys, traceback
import RPi.GPIO as GPIO
import time, os

ledMap = {1:13,2:19,3:26,4:21,5:20}

letters = {"a":
  "###" + "\n" + 
  "# #" + "\n" +
  "###" + "\n" +
  "# #" + "\n" +
  "# #",
  "b":
  "###" + "\n" +
  "# #" + "\n" +
  "###" + "\n" +
  "# #" + "\n" +
  "###",
  "c":
  "###" + "\n" + 
  "#" + "\n" + 
  "#" + "\n" +
  "#" + "\n" +
  "###",
  "d":
  "## " + "\n" + 
  "# #" + "\n" + 
  "# #" + "\n" +
  "# #" + "\n" +
  "##",
  "e":
  "###" + "\n" + 
  "#" + "\n" + 
  "###" + "\n" +
  "#" + "\n" +
  "###",
  "h":
  "# #" + "\n" + 
  "# #" + "\n" + 
  "###" + "\n" +
  "# #" + "\n" +
  "# #",
  "i":
  "###" + "\n" + 
  " # " + "\n" + 
  " # " + "\n" +
  " # " + "\n" +
  "###",
  "l":
  "#" + "\n" + 
  "#" + "\n" + 
  "#" + "\n" +
  "#" + "\n" +
  "###",
  "m":
  "# #" + "\n" + 
  "###" + "\n" + 
  "# #" + "\n" +
  "# #" + "\n" +
  "# #",
  "o":
  "###" + "\n" + 
  "# #" + "\n" + 
  "# #" + "\n" +
  "# #" + "\n" +
  "###",
  "p":
  "###" + "\n" + 
  "# #" + "\n" + 
  "###" + "\n" +
  "#" + "\n" +
  "#",
  "r":
  "###" + "\n" + 
  "# #" + "\n" + 
  "###" + "\n" +
  "## " + "\n" +
  "# #",
  "s":
  "###" + "\n" + 
  "#  " + "\n" + 
  "###" + "\n" +
  "  #" + "\n" +
  "###",
  "t":
  "###" + "\n" + 
  " # " + "\n" + 
  " # " + "\n" +
  " # " + "\n" +
  " # ",
  "u":
  "# #" + "\n" + 
  "# #" + "\n" + 
  "# #" + "\n" +
  "# #" + "\n" +
  "###",
  "v":
  "# #" + "\n" + 
  "# #" + "\n" + 
  "# #" + "\n" +
  "# #" + "\n" +
  " # ",
  "y":
  "# #" + "\n" + 
  "# #" + "\n" + 
  " # " + "\n" +
  " # " + "\n" +
  " # ",
  "'":
  " # " + "\n" + 
  "#  " + "\n" + 
  "   " + "\n" +
  "   " + "\n" +
  "   ",
  " ":
  " " + "\n" + 
  " " + "\n" + 
  " " + "\n" +
  " " + "\n" +
  " "
}

def test1():
  for _ in range(5): #blick LEDs 5 times
    for pin in ledMap.values():
      GPIO.output(pin,True)
      time.sleep(0.1) #blink for 0.1 second
      GPIO.output(pin,False)

def test2():
  sentence = "happy mother's day"
  temp = {0:"", 1:"", 2:"", 3:"", 4:""}
  for letter in sentence.lower():
    lines = letters[letter].split("\n") #Break letter in to vertical lines
    for column in range(0,3): #each letter is 3 wide
      os.system("clear")
      lineNumber = 1
      row = 0
      for line in lines:
        if len(line) > column: #check if the part of the letter has content
          temp[row] += line[column]
        else:
          temp[row] += " "
        row += 1
        lineNumber += 1
      print temp[0], "\n", temp[1], "\n", temp[2], "\n", temp[3], "\n", temp[4]
      time.sleep(0.2)
    temp[0] = temp[0] + " "
    temp[1] = temp[1] + " "
    temp[2] = temp[2] + " "
    temp[3] = temp[3] + " "
    temp[4] = temp[4] + " "
    time.sleep(0.2)

def test3():
  sentence = "happy mother's day"
  temp = {0:"", 1:"", 2:"", 3:"", 4:""}
  for letter in sentence.lower():
    lines = letters[letter].split("\n") #Break letter in to vertical lines
    for column in range(0,3): #each letter is 3 wide
      os.system("clear")
      lineNumber = 1
      row = 0
      for line in lines:
        if len(line) > column: #check if the part of the letter has content
          if line[column] == "#":
            GPIO.output(ledMap[lineNumber],True)
          else:
            GPIO.output(ledMap[lineNumber],False)
          temp[row] += line[column]
        else:
          GPIO.output(ledMap[lineNumber],False)
          temp[row] += " "
        row += 1
        lineNumber += 1
      print temp[0], "\n", temp[1], "\n", temp[2], "\n", temp[3], "\n", temp[4]
      time.sleep(0.2)
    temp[0] = temp[0] + " "
    temp[1] = temp[1] + " "
    temp[2] = temp[2] + " "
    temp[3] = temp[3] + " "
    temp[4] = temp[4] + " "
    for pin in ledMap.values():
      GPIO.output(pin,False)
    time.sleep(0.2)

try:
  GPIO.setmode(GPIO.BCM)
  GPIO.setwarnings(True)

  for pin in ledMap.values():
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
