import random
import PySimpleGUI as sg

class Chute_O_Numero:
    def __init__(self):
        self.valor_aleatorio = 0
        self.valor_minimo = 1
        self.valor_maximo = 100
        self.tentar_novamente = True

    def Iniciar(self):
        #layout
        layout = [
            [sg.Text('Seu Chute:', size=(20,0))],
            [sg.Input(size=(18,0), key='ValorChute')],
            [sg.Button('Chutar')],
            [sg.Output(size=(20,10))]
        ]

        # Janela
        self.janela = sg.Window('Chute O Número!')

        #usar valores





        self.GerarNumeroAleatorio()
        self.PedirValorAleatorio()

        try: 
            while True:
                # receber valores
                self.evento, self.valores = self.janela.Read(layout = layout)
                self.valor_do_chute = self.valores['ValorChute']
                
                if self.evento == "Chutar":
                    while self.tentar_novamente == True:
                        if int(self.valor_do_chute) > self.valor_aleatorio:
                            print('Chute um valor mais baixo.')
                            self.PedirValorAleatorio()
                                    

                        elif int(self.valor_do_chute) < self.valor_aleatorio:
                            print('Chute um valor mais alto.')
                            self.PedirValorAleatorio()
                                    

                        else:
                            print('Você acertou!!')
                            self.tentar_novamente == False
                            break
        except:
            print('digite apenas numeros')
            self.Iniciar()

    def PedirValorAleatorio(self):
        self.valor_do_chute = input('Chute um número: ')
        

    def GerarNumeroAleatorio(self):
        self.valor_aleatorio = random.randint(self.valor_minimo, self.valor_maximo)


chute = Chute_O_Numero()
chute.Iniciar()