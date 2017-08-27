import RPi.GPIO as GPIO
import time
import thread
import click

# Setup GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.OUT)

key = ''
stop = False


def wait_for_key_press():
    """
    listen for keypress and assign the pressed key char to a variable
    :return:
    """

    try:
        while True:
            global key
            global stop
            key = click.getchar()
            print key + " pressed"

    except KeyboardInterrupt:
        stop = True
        print "A keyboard interrupt has been noticed"

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
    while key in ['b', 'B'] and not stop:
        GPIO.output(8, 0)
        time.sleep(0.001)
        GPIO.output(8, 1)
        time.sleep(0.001)


def alternate_slowly():
    """
    alternate the lights slowly
    :return:
    """

    switch_speed = 10
    while key in ['s', 'S'] and not stop:
        if int(round(time.time())) % (switch_speed * 2) < switch_speed:
            GPIO.output(8, 0)
        else:
            GPIO.output(8, 1)
        time.sleep(0.1)

try:
    # start a new thread to listen for keypress
    thread.start_new_thread(wait_for_key_press, ())

    while not stop:
        one_light()
        both_light()
        alternate_slowly()
        # add a small delay in the main loop so the other threads can run
        # [there should be a better way to solve this problem]
        time.sleep(0.01)

except KeyboardInterrupt:
    print "A keyboard interrupt has been noticed"

finally:
    GPIO.cleanup()
