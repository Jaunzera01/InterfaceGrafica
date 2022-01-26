from PySimpleGUI import PySimpleGUI as sg

# Layout (Obs.: veja mais temas aqui: https://www.geeksforgeeks.org/themes-in-pysimplegui/):
sg.theme('TanBlue')
layout = [
    [sg.Text('Nome '),sg.Input(key='usuario',size=(30, 1))],
    [sg.Text('Senha'), sg.Input(key='senha',password_char='*',size=(30, 1))],
    [sg.Checkbox('Deseja salvar o login?')],
    [sg.Button('Entrar')]
]

# Display / Tela:
tela = sg.Window('Tela de Login', layout)

# Eventos:
while True:
    eventos, valores = tela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Entrar':
        if valores['usuario'] == 'fulano' and valores['senha'] == '123321':
            print('Nome: fulano')
            print('Senha: 123321')