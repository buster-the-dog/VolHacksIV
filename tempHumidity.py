import sys, math, json
import RPi.GPIO as GPIO
import time
import Adafruit_DHT

def main():
  humidity, temperature = Adafruit_DHT.read_retry(11, 4)
  return humidity + ' ' + temperature

if __name__ == "__main__":
  print main()