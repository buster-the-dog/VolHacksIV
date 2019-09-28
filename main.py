import sys, math, json
import RPi.GPIO as GPIO
import time
import Adafruit_DHT
import requests

def main():
  targetHumid = 30
  dryingTimeStart = -1
  heaterPort = 2
  GPIO.setwarnings(False)
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(heaterPort, GPIO.OUT)
  
  if len(sys.argv) < 2:
    return "usage: python main.py [targetTemp] [heatingTime]"
  
  targetTemp = int(sys.argv[1])
  humidity, initTemp = Adafruit_DHT.read_retry(11, 4)
  
  try:
    while True:
      humidity, temperature = Adafruit_DHT.read_retry(11, 4)
      temperature, targetTemp, humidity
      if temperature >= targetTemp:
        GPIO.output(heaterPort, GPIO.LOW)
      else:
        GPIO.output(heaterPort, GPIO.HIGH)
      
      if ((targetTemp - 5) < temperature) and dryingTimeStart == -1:
        dryingTimeStart = time.time();
      
      if ((dryingTimeStart + int(sys.argv[2])) <= time.time()) and dryingTimeStart != -1:
        requests.post("https://maker.ifttt.com/trigger/filament_dry/with/key/djmRT5cNql9CJhtenF9aRE")
        GPIO.output(heaterPort, GPIO.LOW)
        return "filament done drying"
      
  except KeyboardInterrupt:
    GPIO.output(heaterPort, GPIO.LOW)
    return "exiting cleanly"

if __name__ == "__main__":
  print main()