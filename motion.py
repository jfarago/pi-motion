import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.IN, GPIO.PUD_DOWN)    #Read output from PIR motion sensor
GPIO.setup(13, GPIO.IN, GPIO.PUD_DOWN)    #Read output from PIR motion sensor
GPIO.setup(7, GPIO.OUT)                   #LED output pin

while True:
  j=GPIO.input(11)
  k=GPIO.input(13)
  if j==0 and k==0:                       #When output from motion sensor is LOW
    GPIO.output(7, 0)                     #Turn off LED
    time.sleep(0.1)
  elif j==1 or k==1:                      #When output from motion sensor is HIGH
    if j == 1:
      print "Jared Motion Detected"
    else:
      print "Krystal Motion Detected"
    print "Turn on lights for 3 minutes"
    GPIO.output(7, 1)                     #Turn ON LED
    time.sleep(180)