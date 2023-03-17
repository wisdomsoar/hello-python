import pyautogui
import time
#regular expression
import re

#python的縮排必須正確，要寫在while底下的敘述，就應該要縮排。
while True:
    window_title = "Advertisement"
    regex = re.compile('.*Advertisement.*', re.IGNORECASE)
    windows = [window for window in pyautogui.getAllWindows() if regex.match(window.title)]

    if len(windows) > 0:
        pyautogui.press('volumemute')
        print(f"Muted audio for window: {window_title}")
        time.sleep(30)
        
        pyautogui.press('volumemute')
        print(f"Unmuted audio for window: {window_title}")
    time.sleep(1)
