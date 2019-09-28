import sys, math, json
import RPi.GPIO as GPIO
import time

def main():
  ledPort = 2
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(ledPort, GPIO.OUT)
  GPIO.output(ledPort, GPIO.HIGH)
  time.sleep(5)
  GPIO.output(ledPort, GPIO.LOW)
  return "Successfully Executed"

if __name__ == "__main__":
  print main()