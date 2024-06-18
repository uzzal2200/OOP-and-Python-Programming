import pyautogui
from time import sleep
sleep(10)
for i in range(0,50):
    pyautogui.write('  I  love you  ',interval=0.01)            
    pyautogui.press('enter')

