#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

servoPIN = 17
channel = 21


GPIO.setmode(GPIO.BCM)  
GPIO.setup(servoPIN, GPIO.OUT)     
GPIO.setup(channel, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def alert(ev=None):
    print("Tilt Detected")
    p = GPIO.PWM(servoPIN, 50) # GPIO 17 for PWM with 50Hz
    p.start(2.5) # Initialization
    p.ChangeDutyCycle(5)
    time.sleep(0.5)
    p.ChangeDutyCycle(17)
    time.sleep(0.5)
    p.stop()


def loop():
    GPIO.add_event_detect(channel, GPIO.FALLING, callback=alert, bouncetime=100) 
    while True:
        pass   

if __name__ == '__main__':
    try:
        loop()
    except KeyboardInterrupt: 
	GPIO.cleanup()