import webbrowser as web

import time
import pyautogui as auto
import time

from settings import webpage, x, y

web.open_new_tab(webpage) 
time.sleep(25) # Wait for the browser upload the page

print("Use automation.")

for i in range(0, 100):
    auto.click(int(x), int(y))
    time.sleep(0.1)

print("It ends.")
