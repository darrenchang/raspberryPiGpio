import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

cathodes = [7, 11, 15]
anodes = [12, 16, 22]
sleep_time = 0.001
speed = 35

# 0 represents LED on, 1 represents LED off
ani = [
    [[1, 0, 1],
     [1, 0, 1],
     [1, 0, 1]],

    [[1, 1, 0],
     [1, 0, 1],
     [0, 1, 1]],

    [[1, 1, 1],
     [0, 0, 0],
     [1, 1, 1]],

    [[0, 1, 1],
     [1, 0, 1],
     [1, 1, 0]],

    [[1, 0, 1],
     [1, 1, 1],
     [1, 0, 1]],

    [[1, 1, 0],
     [1, 1, 1],
     [0, 1, 1]],

    [[1, 1, 1],
     [0, 1, 0],
     [1, 1, 1]],

    [[0, 1, 1],
     [1, 1, 1],
     [1, 1, 0]],
]

for cathode in cathodes:
    GPIO.setup(cathode, GPIO.OUT)
    GPIO.output(cathode, 0)

for anode in anodes:
    GPIO.setup(anode, GPIO.OUT)
    GPIO.output(anode, 0)

try:
    while True:
        for frame in range(len(ani)):
            for pause in range(speed):
                for i in range(3):
                    GPIO.output(cathodes[0], ani[frame][i][0])
                    GPIO.output(cathodes[1], ani[frame][i][1])
                    GPIO.output(cathodes[2], ani[frame][i][2])

                    GPIO.output(anodes[i], 1)
                    time.sleep(sleep_time)
                    GPIO.output(anodes[i], 0)


except KeyboardInterrupt:
    GPIO.cleanup()
