from time import sleep
import RPi.GPIO as GPIO
import _thread
import click

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

m1a = 17
m1b = 18
m2a = 22
m2b = 23

GPIO.setup(m1a,GPIO.OUT) #Set 17 as output (Motor 1 A)
GPIO.setup(m1b,GPIO.OUT) #Set 18 as output (Motor 1 B)
GPIO.setup(m2a,GPIO.OUT) #Set 22 as output (Motor 2 A)
GPIO.setup(m2b,GPIO.OUT) #Set 23 as output (Motor 2 B)

key = ''
stop = False


def wait_for_key_press():
    """
    listen for keypress and assign the pressed key char to a variable
    :return:
    """

    try:
        while not stop:
            global key
            global stop
            key = click.getchar()
            print(key + " pressed")
            if key is "q":
                stop = True

    except KeyboardInterrupt:
        stop = True
        print("A keyboard interrupt has been noticed")


def forwards():
    GPIO.output(m1a, 1)
    GPIO.output(m1b, 0)
    GPIO.output(m2a, 0)
    GPIO.output(m2b, 1)


def backwards():
        GPIO.output(m1a,0)
        GPIO.output(m1b,1)
        GPIO.output(m2a,1)
        GPIO.output(m2b,0)


def turn_right():
    GPIO.output(m1a, 1)
    GPIO.output(m1b, 0)
    GPIO.output(m2a, 1)
    GPIO.output(m2b, 0)


def turn_left():
    GPIO.output(m1a, 0)
    GPIO.output(m1b, 1)
    GPIO.output(m2a, 0)
    GPIO.output(m2b, 1)


def stop_motor():
        GPIO.output(m1a,0)
        GPIO.output(m1b,0)
        GPIO.output(m2a,0)
        GPIO.output(m2b,0)

try:
    # start a new thread to listen for keypress
    _thread.start_new_thread(wait_for_key_press, ())

    while not stop:
        if key is "w":
            forwards()
        if key is "s":
            backwards()
        if key is "d":
            turn_right()
        if key is "a":
            turn_left()
        if key is "e":
            stop_motor()
        sleep(0.01)

except KeyboardInterrupt:
    print("A keyboard interrupt has been noticed")

finally:
    GPIO.cleanup()
