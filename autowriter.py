import pyautogui
import time

time.sleep(3)
with open('code.txt','r')as f:
    lines=f.readlines()
    for line in lines:
    
        pyautogui.write(line.lstrip())
