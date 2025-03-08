import subprocess

import questionary
from questionary import Choice


def run():
    links = [
        "https://aulas.franciscosensaulas.com",
        "https://github.com/franciscosensaulas",
        "https://franciscosensaulas.com/admin/conteudo",
        "https://franciscosens.com",
        "https://api.franciscosens.com",
        "https://excalidraw.com",
        "https://app.sistemaquality.com.br/portal/#/login",
    ]
    links_choices = [Choice(title=link, value=link, checked=True) for link in links]
    links_selected = questionary.checkbox("Selecione os links que deseja abrir: ", choices=links_choices).ask()

    if links_selected:
        subprocess.run(['start', 'chrome', '--start-maximized', *links_selected], shell=True)
