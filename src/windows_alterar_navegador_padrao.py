import subprocess

import pyautogui

from utils import delay


def run():
    # Open the Default Apps settings
    subprocess.run(['start', 'ms-settings:defaultapps'], shell=True)

    # Your next code will wait until the above command finishes
    # print("The 'ms-settings:defaultapps' window is open.")
    delay(1)
    # pyautogui.press(['tab']) # email
    # time.sleep(0.1)
    pyautogui.press(['tab'])  # maps
    delay()
    pyautogui.press(['tab'])  # music
    delay()
    pyautogui.press(['tab'])  # pictures
    delay()
    pyautogui.press(['tab'])  # video
    delay()
    pyautogui.press(['tab'])  # browser
    delay()

    pyautogui.press(['enter'])  # open dialog to choose chrome
    delay()
    pyautogui.press(['enter'])  # change to chrome
    delay()

    # subprocess.run(['taskkill', '/f', '/im', 'SystemSettings.exe'])
