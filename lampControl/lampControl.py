import RPi.GPIO as GPIO
from bluedot import BlueDot
from signal import pause


# Setup GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.LOW)

bd = BlueDot()


def lamp_switch():
    state = GPIO.input(8)
    if state is 0:
        GPIO.output(8, 1)
        print("turned on")
    else:
        GPIO.output(8, 0)
        print("turned off")

try:
    bd.when_pressed = lamp_switch

    pause()

except KeyboardInterrupt:
    print("A keyboard interrupt has been noticed")

finally:
    GPIO.cleanup()
