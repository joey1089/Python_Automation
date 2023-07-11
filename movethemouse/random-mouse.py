# Reference - https://youtu.be/J2c4gHAQalA?t=9 and also
# Reference - https://www.thepythoncode.com/article/control-mouse-python

import pyautogui as pau
import random
import time
import screeninfo
import mouse


# pau.moveTo(400,560)
while True:
    x = random.randint(850,1280)
    y = random.randint(350, 750)
    pau.moveTo(x,y,0.5)
    time.sleep(2)
    print("\n Screen Details - X,Y")
    print(pau.displayMousePosition()) #It will automatically display the location and RGB of the mouse cursor.
    # drag from (0, 0) to (100, 100) relatively with a duration of 0.1s
    # mouse.drag(0, 0, 100, 100, absolute=False, duration=0.1)
    pau.drag(x,y,x,y,0.5)
    pau.click(x,y),pau.click(x,y)

    # print(pau.center())
    # move the mouse and click on something



