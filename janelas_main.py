import PySimpleGUI as sg
from cotacao_janelas import pegar_cotacoes
layout = [
    [sg.Text('Pegar Cotação da Moeda')],
    [sg.InputText(key='nome_cotacao')],
    [sg.Button('Pegar Cotação'),sg.Button('Cancelar')],
    [sg.Text('', key='texto_cotacao')]
]


janela = sg.Window('SISTEMAS DE COTAÇÕES', layout)

while True:
    evento, valores = janela.read() # A cada execução ele irá ler e armazenar os valores e eventos dentro das variaveis
    #Evento = Todo clique que é feito em botão
    #Valores = Sempre que um valor for prenchido será armazenado em valores
    if evento == sg.WIN_CLOSED or evento == 'Cancelar': #WIN_CLOSED = X de fechar aba, faz que encerra a janela
        break
    if evento == 'Pegar Cotação':
        codigo_cotacao = valores['nome_cotacao']
        cotacao = pegar_cotacoes(codigo_cotacao)
        janela['texto_cotacao'].update(f'A cotação do {codigo_cotacao} é de {cotacao}')
        
    


janela.close()