import pyautogui
import time

for i in range (1, 30):
    
    output = pyautogui.locateOnScreen('looksLikeThis.png')
    
    if (output != "None"):
        pyautogui.hotkey('command', 'w')

    time.sleep(1000)
    i = i+1



