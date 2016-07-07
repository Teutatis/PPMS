#!/usr/bin/env python2.7  
#!user/bin/python

# Adapted from code provided on the following web sites
# 'Things Wat I Have Done With My Raspberry Pi' & 'Raspi-TV'
# http://thingswatihavedonewithmyraspberrypi.blogspot.co.uk/2012/10/controlling-bigtrack-motors-with-my.html
# http://raspi.tv/2013/how-to-use-soft-pwm-in-rpi-gpio-pt-2-led-dimming-and-motor-speed-control 

# MOTOR OUTPUT TO CLOCKWISE FOR 10 SECONDS.

# Import required modules.
import time
from time import sleep
import RPi.GPIO as GPIO

# Set GPIO Board numbers to use Raspberry Pi board pin numbers.
GPIO.setmode(GPIO.BOARD)

# Suppress GPIO warnings.
GPIO.setwarnings(False)

# Set up GPIO pins.
GPIO.setup(13, GPIO.OUT)   # Connected to AIN1.
GPIO.setup(7, GPIO.OUT)    # Connected to AIN2.
GPIO.setup(15, GPIO.OUT)   # Connected to STBY.
GPIO.setup(22, GPIO.OUT)   # Connected to PWMA.
# GPIO.setup(31, GPIO.IN) ***WARNING***CHECK VOLTAGE FROM FAN PIN TO RASPI*****

# Motor direction to - Clockwise: AIN1=high & AIN2=low (reverse for anti-clockwise).
GPIO.output(13, GPIO.HIGH) # Set AIN1.
GPIO.output(7, GPIO.LOW)   # Set AIN2.

# Take the brakes off. STBY: high(brakes off) / low=(brakes on).
GPIO.output(15, GPIO.HIGH) # Set STBY.

motor_a = GPIO.PWM(22, 50) # Create object 'motor_a' for PWM (pin, hertz).

pause_time = 0.05          # Create object 'pause_time' to slow down/speed up the counting delay.

motor_a.start(0)           # Start motor_a on 0 percent duty cycle (off)    

max_range = 100


  
# Create loop to increase the duty cycle from 0 to 101 and repeat.
try:  
    while True:  
        for counter in range(0, (max_range+1)): # max_range+1, 101 because it stops when it finishes 100. 
            motor_a.ChangeDutyCycle(counter)    # Change the duty cycle to the current counter value.
            sleep(pause_time)                   # Pause.
            print "\n", counter                 # Print the current counter value to the terminal.
             
except KeyboardInterrupt:    
# Code to run before the program exits when 'CTRL+C' is pressed.  
    motor_a.stop()      # stop the white PWM output    
    GPIO.cleanup()      # clean up GPIO on CTRL+C exit 
  
# except:  
    # This catches ALL other exceptions including errors.  
    # No error messages for debugging.  
    # Use it once your code is working.  
    # print "Teut! - Other error or exception occurred!"  
    # GPIO.cleanup()      # Clean up GPIO on 'CTRL+C'.
  
finally:  
    GPIO.cleanup() # Ensures a clean GPIO exit.
