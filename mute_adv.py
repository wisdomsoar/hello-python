import pyautogui
import time
#regular expression
import re

pyautogui.FAILSAFE = False

#python的縮排必須正確，要寫在while底下的敘述，就應該要縮排。
while True:
    regex = re.compile('.*Advertisement.*', re.IGNORECASE)
    regex2 = re.compile('.*Spotify Free.*', re.IGNORECASE)
    windows = [window for window in pyautogui.getAllWindows() if regex.match(window.title)]
    windows2 = [window for window in pyautogui.getAllWindows() if regex2.match(window.title)]

    if len(windows) > 0 or len(windows2) > 0:
        pyautogui.press('volumemute')
        print(f"Muted audio")
        time.sleep(30)
        
        pyautogui.press('volumemute')
        print(f"Unmuted audio")
    time.sleep(1)
