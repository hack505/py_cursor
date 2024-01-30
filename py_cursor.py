import pyautogui
import keyboard
import random
import time

# starting sleep fo 10 secs
time.sleep(10)

# resolution of victom pc
height = pyautogui.size().height
width = pyautogui.size().width

# To prevent form failsafe which breaks with cursor in corner
pyautogui.FAILSAFE = False

# the main logic to move and break
while True:
#     To break the loop
    if keyboard.is_pressed('ctrl') and keyboard.is_pressed('s'):
        print("breaked")
        break
        
#     To genrete random loc
    x = random.randint(0, width)
    y = random.randint(0, height)
    
#     To move cour
    pyautogui.moveTo(x, y)
    
