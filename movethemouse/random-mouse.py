# Reference - https://youtu.be/J2c4gHAQalA?t=9

import pyautogui as pau
import random
import time
import screeninfo


# pau.moveTo(400,560)
while True:
    x = random.randint(850,1280)
    y = random.randint(350, 750)
    pau.moveTo(x,y,0.5)
    time.sleep(2)
    print("\n Screen details")
    print(pau.displayMousePosition()) #It will automatically display the location and RGB of the mouse cursor.
    # print(pau.center())

