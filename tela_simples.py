import PySimpleGUI as sg

class TelaPython:
    def __init__(self):
        #Tema
        [sg.change_look_and_feel('DarkBlue2')]
        #Layout - Para que o layout funcione precisamos criar uma JANELA
        layout = [
          [sg.Text('LOGIN', size=(10,0)),sg.Input(size=(15,0),key='login')],
          [sg.Text('SENHA', size=(10,0)),sg.Input(size=(15,0),key='senha')],
          [sg.Text('Quais e-mails são aceitos?')],
          [sg.Checkbox('Gmail',key='gmail'),sg.Checkbox('Yahoo',key='yahoo'),sg.Checkbox('Outlook',key='outlook')],#Checkbox = Caixa de texto de seleção
          [sg.Text('Aceita Cartão')],
          [sg.Radio('Sim', 'Cartões',key='aceita_cartao'),sg.Radio('Não', 'Cartões',key='nao_aceita_cartao')],
          [sg.Slider(range(0,100),default_value=0,orientation='h',size=(15,20), key='sliderVelocidade')],
          [sg.Button('CONFIRMAR')],
          [sg.Output(size=(30,10))] #Exibe os dados em um campo visual 
        ]
        #Janela
        janela = sg.Window('Dados do Usuário').layout(layout) #self.janela faz com que ela mantenha a janela aberta sempre, porem depende um lop while True na função de exibição
        #Extrair dados da tela (Unpacking)
        self.button, self.values = janela.Read() #Pega as informações da tela e envia para values

    def Iniciar(self):
        #Exibir as informações que foram extraidas da tela
        nome = self.values['login']
        senha = self.values['senha']
        aceita_gmail = self.values['gmail']
        aceita_yahoo = self.values['yahoo']
        aceita_outlook = self.values['outlook']
        aceita_cartao = self.values['aceita_cartao']
        nao_aceita_cartao = self.values['nao_aceita_cartao']
        velocidade_script = self.values['sliderVelocidade']
        print(f'Login: {nome}')
        print(f'Senha: {senha}')
        print(f'Aceita Gmail: {aceita_gmail}')
        print(f'Aceita Yahoo: {aceita_yahoo}')
        print(f'Aceita Outlook: {aceita_outlook}')        
        print(f'Aceita Cartão: {aceita_cartao}')      
        print(f'Não Aceita Cartão: {nao_aceita_cartao}')      
        print(f'Velocidade Script: {velocidade_script}')


tela = TelaPython()
tela.Iniciar()
