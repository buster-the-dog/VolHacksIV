import sys, math, json
import RPi.GPIO as GPIO
import time

def main():
  ledPort = 2
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(bluePin, GPIO.OUT)
  GPIO.output(ledPort, GPIO.HIGH)
  return "Successfully Executed"

if __name__ == "__main__":
  print main()