import RPi.GPIO as GPIO
from bluedot import BlueDot
from signal import pause


# Setup GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.LOW)

bd = BlueDot()


def lamp_switch_on():
    GPIO.output(8, 1)
    print("turned on")

def lamp_switch_off():
    GPIO.output(8, 0)
    print("turned off")


try:
    bd.when_pressed = lamp_switch_on
    bd.when_released = lamp_switch_off
    pause()

except KeyboardInterrupt:
    print("A keyboard interrupt has been noticed")

finally:
    GPIO.cleanup()
