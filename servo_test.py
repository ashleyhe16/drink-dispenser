# Ashley He (ach238), Amelia Myers (arm298)
# Lab 3, Monday
# 4 November 2019

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(5, GPIO.OUT)
#GPIO.setup(6, GPIO.OUT)
#GPIO.setup(19, GPIO.OUT)
#GPIO.setup(26, GPIO.OUT)
#GPIO.setup(20, GPIO.OUT)
#GPIO.setup(21, GPIO.OUT)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP)

dc = 50

p = GPIO.PWM(5, 1000/21.5)
 
p.start(dc) # duty cycle 50%

# servo control
def GPIO17_callback(channel): 
    print(" ")
    print"Servo, clockwise"
    p.ChangeFrequency(1000/(20+0.75))
    p.ChangeDutyCycle(75/(20+0.75))
    
def GPIO22_callback(channel): 
    print(" ")
    print"Servo, counter-clockwise"
    p.ChangeFrequency(1000/(20+2.25))
    p.ChangeDutyCycle(225/(20+2.25))

def GPIO27_callback(channel): 
    print(" ")
    print"Servo Stop."
    p.ChangeDutyCycle(0) 
    
GPIO.add_event_detect(17, GPIO.FALLING, callback=GPIO17_callback, bouncetime=300)
GPIO.add_event_detect(22, GPIO.FALLING, callback=GPIO22_callback, bouncetime=300)
GPIO.add_event_detect(27, GPIO.FALLING, callback=GPIO22_callback, bouncetime=300)


# bail out
while GPIO.input(23):
    pass

p.stop()
# p.stop()        
GPIO.cleanup()
