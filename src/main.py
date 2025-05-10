import questionary

import windows_alterar_foco
import definir_git
import windows_alterar_navegador_padrao
import abrir_chrome
import windows_dark_mode
from rich.console import Console
from rich.text import Text

opcoes = {
    "Abrir o chrome": abrir_chrome.run,
    "Instalar Git": definir_git.install_git_or_open_chrome,
    "Windows - Dark mode": windows_dark_mode.run,
    "Windows - Alterar navegador padrão": windows_alterar_navegador_padrao.run,
    "Windows - Desabilitar focus": windows_alterar_foco.run,
    "Definir o git global": definir_git.run,
    "Sair": None
}

def __print_is_installed():
    git_is_installed = definir_git.is_git_installed()

    console = Console()
    if git_is_installed:
        text = Text("Git instalado: Sim")
    else:
        text = Text("Git instalado: Não")
    text.stylize("bold magenta", 0, 15)
    console.print(text)


def __ask_menus():
    __print_is_installed()

    menus = [questionary.Choice(titulo, value=runner) for titulo, runner in opcoes.items()]
    handler = ""
    while handler != "Sair":
        handler = questionary.select("Escolha o menu desejado: ", menus).ask()

        if handler != "Sair":
            handler()


def __main__():
    try:
        __ask_menus()
    except Exception as e:
        print("Error happend", e)


if __name__ == "__main__":
    __main__()
