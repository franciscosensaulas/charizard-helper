import subprocess

import questionary

import install_git


def is_git_installed():
    try:
        # Executa o comando git --version para verificar se o Git está instalado
        result = subprocess.run(['git', '--version'], capture_output=True, text=True, check=True)
        # Se o comando for bem-sucedido, o Git está instalado
        # print(f"Git está instalado: {result.stdout.strip()}")
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        # Se o comando falhar, o Git não está instalado
        # print("Git não está instalado ou não está disponível no PATH.")
        return False


def __get_git_config(config_key):
    try:
        # Executa o comando git para obter o valor da configuração especificada
        result = subprocess.run(['git', 'config', '--global', config_key],
                                capture_output=True, text=True, check=True)
        return result.stdout.strip()
    except (subprocess.CalledProcessError, FileNotFoundError):
        return None


def __set_git_config(config_key, value):
    try:
        # Executa o comando git config para definir a configuração especificada
        subprocess.run(['git', 'config', '--global', config_key, value], check=True)
        # print(f"Git {config_key} definido para: '{value}'")
    except subprocess.CalledProcessError as e:
        print(f"Erro ao definir a configuração do Git: {e}")


def __set_git_global_config(config_key: str, config_value_new: str):
    config_value_current = __get_git_config(config_key)
    if config_value_current:
        print(f"A configuração Git '{config_key}' é: '{config_value_current}'.")
    else:
        print(f"A configuração Git '{config_key}' não está definida.")
    config_value_new = questionary.text(f"Informe o {config_key}?", default=config_value_new).ask()

    __set_git_config(config_key, config_value_new)


def install_git_or_open_chrome():
    abrir_navegador = questionary.confirm("Deseja abrir a página de download do git?").ask()

    if abrir_navegador:
        subprocess.run(['start', 'chrome', '--start-maximized', "https://git-scm.com/downloads/win"], shell=True)
        return

    instalar_silent_git = questionary.confirm("Deseja instalar o git automaticamente?").ask()
    install_git.run(instalar_silent_git)


def run():
    if not is_git_installed():
        print("Git não está instalado ou não está disponível no PATH.")
        return
    print()
    __set_git_global_config("user.name", "Francisco Lucas Janesch Lange Sens")
    print()
    __set_git_global_config("user.email", "franciscosensaulas@gmail.com")
    print()
