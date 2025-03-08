import questionary

import windows_alterar_foco
import definir_git
import windows_alterar_navegador_padrao
import abrir_chrome
import windows_dark_mode

opcoes = {
    "Windows - Dark mode?": windows_dark_mode.run,
    "Windows - Alterar navegador padrão?": windows_alterar_navegador_padrao.run,
    "Windows - Desabilitar focus?": windows_alterar_foco.run,
    "Abrir o chrome?": abrir_chrome.run,
    "Definir o git --global?": definir_git.run,
}


def __ask_menus():
    for title, handler in opcoes.items():
        should_run = questionary.confirm(title).ask()

        if should_run:
            handler()


def __main__():
    try:
        __ask_menus()
    except Exception as e:
        print("Error happend", e)


if __name__ == "__main__":
    __main__()
