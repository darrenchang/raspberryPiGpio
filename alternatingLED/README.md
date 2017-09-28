# Alternating LED
Control two LEDs using only one GPIO pin.
- When one LED is turned on, the other will be off.
- Both LEDs can be on at the same time using multiplex.

# How to use
1. Prepare the circuit on a as shown below. (A bread board is recommended)<br>
![](https://easyeda.com/normal/alternatingLED-decf7f5ac7a64151aca0928aa86bf797)
2. Execute [alternatingLED.py](alternatingLED.py) using "sudo". (root 
permission is required to use GPIO on Raspberry Pi)

## Controls
- press "L" to switch on left light
- press "R" to switch on right light
- press "S" to switch the lights slowly <br>
- press "B" to switch on both light <br>
(The lights will be dimmer than when only when one light is on. This is because
each light is actually only turned on half of the time.)
- press "control + C" one to exit key listener, and press "control + C" again 
to exit the Python program.

# Known issues
- When the program is not running, the light with anode (+) connected to GPIO
pin is slightly lit up, possibly because a small amount of current leaks from 
the 3.3v pin. (it's really hard to see unless you place the lights in really 
dark place)
- The light with anode (+) connected to GPIO pin is slightly brighter than the 
other one possibly because a small amount of current leak from the 3.3v pin. 
You can compare the brightness by turning on both lights.

## Possible fix
- I don't know :/

# Related links
[EasyEDA project link](https://easyeda.com/darrenchang951/simepleCircuit-2db9573acd0b414a9f736e7b6b6cfdd0)