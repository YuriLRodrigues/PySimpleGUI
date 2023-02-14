import PySimpleGUI as sg

# Criar janelas e estilos (layout)
def tela_login_senha():
    sg.theme('DarkGrey5')
    layout = [
        [sg.Text('LOGIN')],
        [sg.Text('SENHA')],
        [sg.Button('ACESSAR')]
    ]
    return sg.Window('Acesso a conta', layout= layout, finalize=True)

def modificar_usuario():
    sg.theme('DarkGrey5')
    layout = [
        [],
        [],
        [],
    ]
# Criar as janelas iniciais

# Criar um loop de leitura de eventos

# Lógica de o que deve acontecer ao clicar os botões