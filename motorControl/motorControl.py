#RTK-000-001 Basis
#Licensed under the GNU GPL V3 License
#(C) Ryanteck LTD. 2014
#Contributors: Ryan Walmsley, Michael Horne
from time import sleep #We will need to sleep the code at points
import RPi.GPIO as GPIO #Import the GPIO library as GPIO

#Setup GPIO
GPIO.setmode(GPIO.BCM) # Set the numbers to Broadcom Mode
GPIO.setwarnings(False) # Ignore any errors

#Assign variables to pins
m1a = 17
m1b = 18
m2a = 22
m2b = 23

GPIO.setup(m1a,GPIO.OUT) #Set 17 as output (Motor 1 A)
GPIO.setup(m1b,GPIO.OUT) #Set 18 as output (Motor 1 B)
GPIO.setup(m2a,GPIO.OUT) #Set 22 as output (Motor 2 A)
GPIO.setup(m2b,GPIO.OUT) #Set 23 as output (Motor 2 B)

#Make both motors go forwards
def forwards():
        GPIO.output(m1a,1) # Motor 1 Forwards turn on
        GPIO.output(m1b,0) # Motor 1 Backwards turn off
        GPIO.output(m2a,1) # Motor 2 Forwards turn on
        GPIO.output(m2b,0) # Motor 2 Backwards turn off

##All off
def stop():
        GPIO.output(m1a,0) # Motor 1 Forwards turn off
        GPIO.output(m1b,0) # Motor 1 Backwards turn off
        GPIO.output(m2a,0) # Motor 2 Forwards turn off
        GPIO.output(m2b,0) # Motor 2 Backwards turn off

#Forever
try:
        while True:
            #Turn motors forward
            print "forwards"
            forwards()
            #sleep for 1 second
            sleep(10)
            #Stop
            print "stop"
            stop()
            #sleep 1 second
            sleep(10)

except (KeyboardInterrupt):
    print "A keyboard interrupt has been notitced"

except:
    print "An error or exception has occured!"

finally:
    GPIO.cleanup()
