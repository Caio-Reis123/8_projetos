# Simulador de Dado
import random
import PySimpleGUI as sg



class SimuladorDeDado:
    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 6
        self.mensagem = 'Você gostaria de gerar um novo valor para o dado? '

        # Layout
        self.layout = [
            [sg.Text('Jogar o dado?')],
            [sg.Button('Sim'), sg.Button('Não')]
            
        ]
    
    def Iniciar(self):
        # Criar uma janela
        self.janela = sg.Window('Simulador de Dado', layout = self.layout)

        # Ler os valores da tela
        self.eventos, self.valores = self.janela.Read()

        # Fazer alguma coisa com esses valores
        try:
            if self.eventos == 'Sim' or self.eventos == 'S':
                msg = self.GerarValorDoDado()
            
            elif self.eventos == 'Não' or self.eventos == 'N':
                msg = ('Obrigado, volte sempre')
                print(msg)
                
            else:
                msg = ('Por favor digitar sim ou não')
                print(msg)
        except:
            msg = ('ocorreu um erro')
            print(msg)

    def GerarValorDoDado(self):
        rolled = (random.randint(self.valor_minimo, self.valor_maximo))
        print(rolled)

simulador = SimuladorDeDado()
simulador.Iniciar()