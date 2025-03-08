import subprocess
from enum import Enum

import pyautogui
import uiautomation
import time

class Acao(Enum):
    ENTRAR = "entrar"
    PROXIMO = "proximo"
    ESPACE = "espaco"


def run():
    acoes_focus = [
        {"titulo": "Desativado", "acao": Acao.ESPACE},
        {"titulo": "Quando minha tela estiver duplicada", "acao": Acao.PROXIMO},
        {"titulo": "Quando minha tela estiver duplicada", "acao": Acao.ESPACE},
        {"titulo": "Quando eu estiver jogando", "acao": Acao.PROXIMO},
        {"titulo": "Quando eu estiver jogando", "acao": Acao.ESPACE},
        {"titulo": "Quando eu estiver usando um app no modo de tela inteira", "acao": Acao.PROXIMO},
        {"titulo": "Quando eu estiver usando um app no modo de tela inteira", "acao": Acao.ESPACE},
    ]

    # Launch Windows Settings using subprocess
    subprocess.run('start ms-settings:quiethours', shell=True)

    # Wait for the app to open (adjust the time if necessary)
    time.sleep(2)

    # pyautogui.press([*"Assistente de foco"])
    focused_text = ""
    for acao_focus in acoes_focus:
        texto = acao_focus["titulo"]
        acao = acao_focus["acao"]

        while True:
            pyautogui.press('tab')

            # Find the focused control after the app is open
            focused_element = uiautomation.GetFocusedControl()

            # Check if the focused element is found
            if focused_element:
                focused_text = focused_element.Name  # Extract the text of the focused element
                if focused_text == texto:
                    if acao == Acao.ESPACE:
                        pyautogui.press('space')


                    print(f"Focused Element Text: {focused_text}")
                    break
