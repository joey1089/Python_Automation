#reference - https://www.youtube.com/watch?v=ms42RwgAGKQ\
#Use case for automation of desktop apps
#status - not working as expected - code needs updates
import pyautogui as pag
import random
import time

curr_coords = pag.position() #current position of the mouse
afk_counter = 0 #away from the keys
while True:
    if pag.position() == curr_coords:
        afk_counter += 1
    else:
        afk_counter = 0 
        curr_coords = pag.position()
    if afk_counter > 5:
        x = random.randint(450,750)
        y = random.randint(1,800)
        pag.moveTo(x,y)
        curr_coords = pag.position()
    print(f"AFK Counter: {afk_counter}")
    time.sleep(2)


