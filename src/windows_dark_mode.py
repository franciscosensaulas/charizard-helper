import subprocess
import time
from enum import Enum

import pyautogui
import uiautomation


class Acao(Enum):
    ENTRAR = "entrar"
    PROXIMO = "proximo"
    ESPACE = "espaco"


def run():
    # Launch Windows Settings using subprocess
    subprocess.run('start ms-settings:', shell=True)

    # Wait for the app to open (adjust the time if necessary)
    time.sleep(1)

    pyautogui.press([*"Escolher a cor de destaque"])
    time.sleep(1)

    pyautogui.press('enter')
    time.sleep(0.1)
    pyautogui.press('enter')
    time.sleep(0.1)

    pyautogui.press('tab')
    pyautogui.press('tab')
    focused_element = uiautomation.GetFocusedControl()

    if focused_element:
        focused_text = focused_element.Name
        print(f"Focused Element Text: {focused_text}")
        pyautogui.press('enter')
        pyautogui.press('e')
        pyautogui.press('enter')
