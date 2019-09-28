import sys, math, json
import RPi.GPIO as GPIO
import time
import Adafruit_DHT

def main():
  targetTemp = 50
  targetHumid = 30
  dryingTime = -1
  heaterPort = 2
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(heaterPort, GPIO.OUT)
  o = GPIO.PWM(heaterPort, 45)
  o.start(100)
  
  try:
    while True:
      humidity, temperature = Adafruit_DHT.read_retry(11, 4)
      #turn heater/fan on
      e = (targetTemp - temperature) / targetTemp
      print e, temperature
      if e < 0:
        e = 0
      o.ChangeDutyCycle(e * 100)
  except KeyboardInterrupt:
    GPIO.output(heaterPort, GPIO.LOW)
    return "exiting cleanly"

if __name__ == "__main__":
  print main()