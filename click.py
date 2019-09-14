import webbrowser as web
import sys

import time
import pyautogui as auto
import time

from settings import webpage, x, y

times = int(sys.argv[1])

web.open_new_tab(webpage) 
time.sleep(25) # Wait for the browser upload the page

print("Use automation.")

for i in range(0, times):
    auto.click(int(x), int(y))
    time.sleep(0.5)

print("It ends.")
