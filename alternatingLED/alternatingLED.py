import RPi.GPIO as GPIO
import time
import thread
import click

GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.OUT)

key = ''

def waitForKeyPress():
    try:
        while True:
            global key
            key = click.getchar()
            print key
    except (KeyboardInterrupt):
        pass
    finally:
        pass
        

def oneLight():
    if key == 'r':
            # print ("right light is on")
            GPIO.output(8, 1)
            # time.sleep(0.0001)
    if key == 'l':
            # print ("left light is on")
            GPIO.output(8, 0)
            # time.sleep(0.0001)

def bothLight():
    while key == 'b':
        GPIO.output(8, 0)
        time.sleep(0.0001)
        GPIO.output(8, 1)
        time.sleep(0.0001)

try:
    # start a new thread to listen for keypress
    thread.start_new_thread(waitForKeyPress, ())

    while True:
        oneLight()
        bothLight()
        # add a small delay in the main loop so the other threads can run
        # [there should be a better way to solve this problem]
        time.sleep(0.001)

except (KeyboardInterrupt):
    print "A keyboard interrupt has been notitced"

except:
    print "An error or exception has occured!"

finally:
    GPIO.cleanup()
