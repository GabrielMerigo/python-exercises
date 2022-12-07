class Jogador:
    def __init__(self, nome, numero, posicao):
        self.__numero = numero
        self.__nome_jogador = nome
        self.__posicao = posicao # GOLEIRO ou DEFESA ou MEIO-CAMPO ou ATECANTE
        self.__situacao = "NORMAL"  # ou "EXPULSO"
        self.__participou_partida = False # ou True

    def getNumero(self):
      return f'{self.__numero}'

    def getNomeJogador(self):
      return f'{self.__nome_jogador}'

    def getPosicao(self):
      return f'{self.__posicao}'

    def getSituacao(self):
      return f'{self.__situacao}'

    def getParticipouPartida(self):
      return f'{self.__participou_partida}'
    
    
def encontrarJogador(lista, numeroJogador):
  for jogador in lista:
    if jogador.getNumero() == numeroJogador:
        return jogador


lst_jogadores = []
lst_escalados = []
lst_reserva = []
message = "MENU \n 1- Ler arquivo de jogadores \n 2- Escalar time \n 3- Realizar Substiuição \n 4- Expulsão \n 5- Imprimir escalação \n Escolha: "

def opcao1():
  with open("convocados.txt", "r",) as arquivo:
    jogadoresDoArquivo = arquivo.read().split("\n")
    for jogadorDoArquivo in jogadoresDoArquivo:
      itemDoJogador = jogadorDoArquivo.split(":")
      jogadorAtual = Jogador(itemDoJogador[1], itemDoJogador[0], itemDoJogador[2])
      lst_jogadores.append(jogadorAtual)
      print(f'Jogador {itemDoJogador[1]} escalado!')
    
    print('Todos os Jogadores foram escalados!')

def opcao2():
  while lst_escalados.__len__() <= 3:
    numeroJogador = input("Digite o número do jogador que será escalado: ")
    jogadorExiste = encontrarJogador(lst_escalados, numeroJogador)
    
    if jogadorExiste != None:
      print(f'Jogador {jogadorExiste.getNomeJogador()} já está escalado...')
    else:
      jogadorParaEscalar = encontrarJogador(lst_jogadores, numeroJogador)
      jogadorParaEscalar.participou_partida = True
      lst_escalados.append(jogadorParaEscalar)
      print(f'Jogador {jogadorParaEscalar.getNomeJogador()} escalado!')
  
  for jogador in lst_jogadores:
    jogadorEstaEscalado = encontrarJogador(lst_escalados, jogador.getNumero())
    if jogadorEstaEscalado == None:
      lst_reserva.append(jogador)
      
def removerJogador(lista, numeroJogador):
    for index, jogador in enumerate(lista):
      if jogador.getNumero() == numeroJogador:
        lista.pop(index)
        
def adicionarJogador(lista, numeroJogador):
  for jogador in lst_jogadores:
    if jogador.getNumero() == numeroJogador:
      lista.append(jogador)
      return jogador

def opcao3():
  numeroJogadorQueSai = input('Digite o número do jogador que irá sair: ')
  numeroJogadorQueEntra = input('Digite o número do jogador que irá entrar: ')
  
  removerJogador(lst_escalados, numeroJogadorQueSai)
  removerJogador(lst_reserva, numeroJogadorQueEntra)
  
  jogadorQueEntrou = adicionarJogador(lst_escalados, numeroJogadorQueEntra)
  jogadorQueSaiu = adicionarJogador(lst_reserva, numeroJogadorQueSai)
  
  print(f'Substituição feita! \n Sai: {jogadorQueSaiu.getNomeJogador()} ↓ \n Entra: {jogadorQueEntrou.getNomeJogador()} ↑')

def opcao4():
  numeroJogadorExpulso = input('Digite o número do jogador expulso: ')
  removerJogador(lst_escalados, numeroJogadorExpulso)
  
  jogadorExpulso = adicionarJogador(lst_reserva, numeroJogadorExpulso)
  print(f'o Jogador expulso foi o {jogadorExpulso.getNomeJogador()} e ele já está no banco de reservas')

def opcao5():
  print('print R')

def init():
    resposta = input(message)

    if resposta == "1":
      opcao1()
    elif resposta == "2":
      opcao2()
    elif resposta == "3":
      opcao3()
    elif resposta == "4":
      opcao4()

while True:
  init()
