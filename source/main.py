import os
import time
import random
import pyautogui


# ------------------------------------------------------------------------------------------------------------#
# Functions
# ------------------------------------------------------------------------------------------------------------#


# Os ---------------------------------------------------------------------------------------------------------#


def abrir(directory: str):
    os.startfile(directory)


# Pyautogui --------------------------------------------------------------------------------------------------#


def escrever(text: str, clock: float = 0, realist=False):
    pressionar('ctrl', 'a')
    pressionar('backspace')
    if realist:
        for letra in text:
            pyautogui.write(letra)
            time.sleep(random.random() / clock)
    else:
        pyautogui.write(text)


def waint_is_present(image, clock: int = 10):
    for i in range(clock):
        time.sleep(1)
        try:
            button = pyautogui.locateCenterOnScreen(image, confidence=0.9)
            assert button is not None
            return True
        except:
            clock -= 1
        if clock <= 0:
            return False


def waint_not_is_present(image, loop: int = 10):
    for i in range(loop):
        try:
            button = pyautogui.locateCenterOnScreen(image, confidence=0.9)
            assert button is None
            return True
        except:
            loop -= 1
        if loop <= 0:
            return False


def clickar(image: str, double_clicks=False, need_click=True, right=False, time: int = 20, confidense=True, move=False, x: int = 0, y: int = 0):
    for i in range(time):
        try:
            if confidense:
                button = pyautogui.locateCenterOnScreen(image, confidence=0.9)
            else:
                button = pyautogui.locateCenterOnScreen(image)

            assert button is not None

            if move:
                if need_click:
                    if right:
                        pyautogui.rightClick(button[0] + x, button[1] + y)
                    else:
                        if double_clicks:
                            pyautogui.doubleClick(button[0] + x, button[1] + y)
                        else:
                            pyautogui.click(button[0] + x, button[1] + y)
                else:
                    pyautogui.moveTo(button[0] + x, button[1] + y)
            else:
                if need_click:
                    if right:
                        pyautogui.rightClick(button)
                    else:
                        if double_clicks:
                            pyautogui.doubleClick(button)
                        else:
                            pyautogui.click(button)
            break
        except:
            time -= 1
        if time == 0:
            print('Infelizmente não foi possivel clickar no botão especificado.\n')


def clickar_como_humano(image: str, right=False, confidense=True):
    loop = 10
    for i in range(loop):
        try:
            if confidense:
                button = pyautogui.locateOnScreen(image, confidence=0.9)
            else:
                button = pyautogui.locateOnScreen(image)
            assert button is not None
            if right:
                pyautogui.rightClick(button[0] + random.randint(0, button[2]) / 1.5,
                                     button[1] + random.randint(0, button[3]) / 1.5)
            else:
                pyautogui.click(button[0] + random.randint(0, button[2]) / 1.5,
                                button[1] + random.randint(0, button[3]) / 1.5)
            break
        except:
            loop -= 1
        if loop == 0:
            print('Infelizmente não foi possivel clickar no botão especificado.\n')


def pressionar(key1, key2=None, presses: int = 1):
    for i in range(presses):
        if key2:
            pyautogui.hotkey(key1, key2)
        else:
            pyautogui.press(key1)


# Others -----------------------------------------------------------------------------------------------------#


def mudar_para_pasta_raiz():
    loc = os.getcwd()
    new_loc = loc.split('\\')
    os.chdir(loc.replace(r'\{}'.format(new_loc[-1]), ''))


def preencher_email():
    # Preenchendo email
    clickar_como_humano(email_button)
    pressionar('ctrl', 'a')
    pressionar('backspace')
    abrir(keepass_locator)
    clickar(copy_user)
    print('Email copiada.\n')
    pressionar('alt', 'tab')
    clickar_como_humano(email_button)
    pressionar('ctrl', 'v')


def preencher_senha():
    # Preenchendo senha
    clickar_como_humano(password_button)
    pressionar('ctrl', 'a')
    pressionar('backspace')
    abrir(keepass_locator)
    clickar(copy_password)
    print('Senha copiada.\n')
    pressionar('alt', 'tab')
    clickar_como_humano(password_button)
    pressionar('ctrl', 'v')


def apertar_enter():
    # Apertando em entrar
    clickar_como_humano(enter_button)
    assert_message = 'Email invalido.'
    assert waint_is_present(invalid_email) is False, assert_message
    assert_message = 'Senha incorreta.'
    assert waint_is_present(invalid_password) is False, assert_message


# ------------------------------------------------------------------------------------------------------------#
# Variables
# ------------------------------------------------------------------------------------------------------------#


# Others
url = "https://www.duolingo.com/?isLoggingIn=true"

# Locators
image_folders = r'.\assets\img'
tor_locator = r'C:\Tor Browser\Browser\firefox.exe'
keepass_locator = r'C:\Program Files\KeePassXC\KeePassXC.exe'

# Images
key = r'{}\key.png'.format(image_folders)
loaded = r'{}\loaded.png'.format(image_folders)
unlock = r'{}\unlock.png'.format(image_folders)
cancel = r'{}\cancel.png'.format(image_folders)
opended_tor = r'{}\tor.png'.format(image_folders)
enter_button = r'{}\enter.png'.format(image_folders)
email_button = r'{}\email.png'.format(image_folders)
copy_user = r'{}\copy_user.png'.format(image_folders)
close_tor = r'{}\close_tor.png'.format(image_folders)
search_button = r'{}\search.png'.format(image_folders)
password_button = r'{}\password.png'.format(image_folders)
login_button = r'{}\login_button.png'.format(image_folders)
copy_password = r'{}\copy_password.png'.format(image_folders)
invalid_email = r'{}\invalid_email.png'.format(image_folders)
portuguese_language = r'{}\portuguese.png'.format(image_folders)
change_language = r'{}\change_language.png'.format(image_folders)
invalid_password = r'{}\invalid_password.png'.format(image_folders)


# ------------------------------------------------------------------------------------------------------------#
# Source
# ------------------------------------------------------------------------------------------------------------#


def Init():
    print('Iniciando projeto.\n')
    mudar_para_pasta_raiz()
    print('Pasta atual:', os.getcwd(), '\n')


def Keepass():
    abrir(keepass_locator)
    print('Keepass aberto.\n')


def Passowrd():
    # Esperando a pesssoa digitar a senha para abrir o banco de dados.
    assert_message = 'Tempo expirado. Imagem não encontrada.\n'

    waint_is_present(unlock, 5)
    assert waint_not_is_present(unlock, 400) is True, assert_message
    print('Bando de dados aberto.\n')


def DataBase():
    # Pegando o user name para logar no site.
    assert_message = 'Duolinguo não encontrado no banco e dados.\n'

    if waint_is_present(cancel) is True:
        clickar(cancel)
    clickar(search_button, move=True, x=100)
    escrever('Duolinguo')
    assert waint_is_present(key) is True, assert_message
    clickar(key, double_clicks=True)
    clickar(copy_user)


def Tor():
    assert_message = 'Não conseguimos visualizar o Tor Browser aberto.\n'

    # Abrindo o Tor Browser.
    abrir(tor_locator)

    if waint_is_present(close_tor) is True:
        clickar(close_tor)
        print('Abrindo uma nova sessão do Tor Browser.')

    assert waint_is_present(opended_tor, clock=60) is True, assert_message
    print('Tor aberto.\n')

    # Entrando no site.
    clickar(opended_tor, move=True, x=100)
    escrever(url)
    pressionar('enter')


def ButtonLogin():
    assert_message = 'Não conseguimos abrir o site.\n'

    # Esperando a pagina carregar.
    assert waint_is_present(loaded, clock=60) is True, assert_message

    # Caso não encontre o botão de login, troque a linguagem do site para portugues.
    if waint_is_present(login_button) is False:
        assert_message = 'Não conseguimos trocar a linguagem do site.\n'

        # Trocando a linguagem do site para portugues
        assert waint_is_present(change_language) is True, assert_message
        clickar(change_language, confidense=False, need_click=False)
        clickar_como_humano(portuguese_language)
        print('A linguagem do site agora e Portugues.')
        clickar_como_humano(login_button)
        print('Fazendo loguin.\n')

    # Mas, se encontar, clickar sobre ele.
    else:
        clickar_como_humano(login_button)
        print('Fazendo login.\n')


def Login():
    # Esperando a pagina carregar.
    assert_message = 'Não conseguimos abrir o site.\n'
    assert waint_is_present(loaded, clock=60) is True, assert_message

    # Preenchendo email
    preencher_email()

    # Preenchendo Senha
    preencher_senha()

    # Apretando em entrar
    apertar_enter()


# ------------------------------------------------------------------------------------------------------------#
# Init
# ------------------------------------------------------------------------------------------------------------#


# Chamando todo o source
Init()
Keepass()
Passowrd()
DataBase()
Tor()
ButtonLogin()
Login()
