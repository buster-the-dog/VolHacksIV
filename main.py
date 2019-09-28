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
  GPIO.output(heaterPort, GPIO.LOW)
  
  try:
    while True:
      humidity, temperature = Adafruit_DHT.read_retry(11, 4)
      #turn heater/fan on
      print humidity, ' ', temperature
      if temperature >= targetTemp:
        #turn heater off
        #log time and wait for it to stay for a while, if humidity is still too low raise target temp
        GPIO.output(heaterPort, GPIO.LOW)
        if dryingTime == -1:
          dryingTime = time.clock()
        if dryingTime == 3600 * 3:
          #drying is done here, return
          return dryingTime
    return humidity, temperature
  except KeyboardInterrupt:
    GPIO.output(heaterPort, GPIO.LOW)
    return "exiting cleanly"

if __name__ == "__main__":
  print main()