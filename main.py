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
  o = GPIO.PWM(heaterPort, 30)
  o.start(100)
  
  try:
    while True:
      humidity, temperature = Adafruit_DHT.read_retry(11, 4)
      #turn heater/fan on
      e = (targetTemp - temperature) / targetTemp
      o.ChangeDutyCycle(e * 100)
  except KeyboardInterrupt:
    GPIO.output(heaterPort, GPIO.LOW)
    GPIO.cleanup()
    return "exiting cleanly"

if __name__ == "__main__":
  print main()