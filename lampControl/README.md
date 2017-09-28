# Lamp control
Turn on and off a 5V (5W) lamp using [Blue Dot](http://bluedot.readthedocs.io/)
- when the dot is pressed, the lamp will be turned on
- when the dot is released, the lamp will be turned off

## How to use
1. Prepare the circuit on a as shown below. (A bread board is recommended)<br>
![](https://easyeda.com/thumbnail/Lamp_Remote_Switch-2baa493a78684549bfac874557bcf130) 
2. Install [Blue Dot app](https://play.google.com/store/apps/details?id=com.stuffaboutcode.bluedot)
on your Android device.
3. Pair your raspberry pi and android device
4. install required python library
``` bash
sudo apt-get install python3-dbus
sudo pip3 install bluedot
```
4. Execute [lampControl.py](lampControl.py) using "sudo". (root 
permission is required to use GPIO on Raspberry Pi)
``` bash
sudo python3 lampControl.py
```

### Controls
- press and hold the blue dot on your phone to turn on the light
- release the blue dot to turn off the light 

## Related links
[EasyEDA project link](https://easyeda.com/Darren%20Chang/Lamp_Remote_Switch-aba127b5ec6b46fb83a39d7437656e39)
[bluedot](http://bluedot.readthedocs.io/en/latest/gettingstarted.html)