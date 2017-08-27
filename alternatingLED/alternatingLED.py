import RPi.GPIO as GPIO
import time
import thread
import click

# Setup GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.OUT)

key = ''


def wait_for_key_press():
    """
    listen for keypress and assign the pressed key char to a variable
    :return:
    """
    try:
        while True:
            global key
            key = click.getchar()
            print key
    except KeyboardInterrupt:
        pass
    finally:
        pass


def one_light():
    if key in ['r', 'R']:
            # print ("right light is on")
            GPIO.output(8, 1)
            # time.sleep(0.0001)
    if key in ['l', 'L']:
            # print ("left light is on")
            GPIO.output(8, 0)
            # time.sleep(0.0001)


def both_light():
    while key in ['b', 'B']:
        GPIO.output(8, 0)
        time.sleep(0.0001)
        GPIO.output(8, 1)
        time.sleep(0.0001)


def alternate_slowly():
    """
    alternate the lights slowly
    :return:
    """
    while key in ['s', 'S']:
        GPIO.output(8, 0)
        time.sleep(0.5)
        GPIO.output(8, 1)
        time.sleep(0.5)

try:
    # start a new thread to listen for keypress
    thread.start_new_thread(wait_for_key_press, ())

    while True:
        one_light()
        both_light()
        alternate_slowly()
        # add a small delay in the main loop so the other threads can run
        # [there should be a better way to solve this problem]
        time.sleep(0.001)

except KeyboardInterrupt:
    print "A keyboard interrupt has been notitced"

except:
    print "An error or exception has occured!"

finally:
    GPIO.cleanup()
