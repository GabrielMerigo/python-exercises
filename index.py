"""
Faça um algoritmo que utilize o menu abaixo:
MENU
======
1- Ler arquivo de jogadores
2- Escalar time
3- Realizar Substiuição
4- Expulsão
5- Imprimir escalação
Escolha: 
Opção 1: Ler de um arquivo texto todos os jogadores
        escalados para a copa e armazenar em uma
        lista (lst_jogadores)
        Cada Elemento da lista será uma instância
            da classe Jogador.
Opção 2: Você deverá escalar 11 dos jogadores para
        iniciar a partida.
        Os Jogadores escalados para a partida ficam
            em uma lista (lst_escalados)
            Alterar o atributo 'participou_partida'
                para True
        Os jogadores que não forem escalados para
            iniciar a partida ficam em uma outra
            lista (lst_reserva)
Opção 3: Você poderá realizar a substituição de um
        jogador por outro.
        Quando isso acontecer o jogador vai para
            a lista de Reserva e o outro para a
            lista Escalados.
Opção 4: Caso haja alguma expulsão, o jogador sai
        da lista de Escalados e vai para a lista
        Reserva.
Opção 5: Mostrar a escalação de todos jogadores que
        participaram do jogo, inclusive as substituições
        e expulsões. 
        Salve esses dados em um arquivo (todosjogadores.txt)
class Jogador:
    def __init__(self, nome, numero, posicao):
        self.__numero = numero
        self.__nome_jogador = nome
        self.__posicao = posicao # GOLEIRO ou DEFESA ou MEIO-CAMPO ou ATECANTE
        self.__situacao = "NORMAL"  # ou "EXPULSO"
        self.__participou_partida = False # ou True
"""
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


lst_jogadores = []
lst_escalados = []
lst_reserva = []
message = "MENU \n 1- Ler arquivo de jogadores \n 2- Escalar time \n 3- Realizar Substiuição \n 4- Expulsão \n 5- Imprimir escalação \n Escolha: "

def opcao1():
  with open("convocados.txt", "r",) as arquivo:
    jogadoresDoArquivo = arquivo.read().split("\n")
    jogadoresDoArquivo.pop()
    for jogadorDoArquivo in jogadoresDoArquivo:
      itemDoJogador = jogadorDoArquivo.split(":")
      jogadorAtual = Jogador(itemDoJogador[1], itemDoJogador[0], itemDoJogador[2])
      lst_jogadores.append(jogadorAtual)

def opcao2():
  print("----- LISTA DE JOGADORES QUE PODEM SER ESCALADOS -----")
  for jogadorParaEscalar in lst_jogadores:
    print(f'Número: {jogadorParaEscalar.getNumero()} | Nome: {jogadorParaEscalar.getNomeJogador()} | Posição: {jogadorParaEscalar.getPosicao()}')

  print("----- Você deve escalar 11 jogadores -----")
  while lst_escalados.__len__() <= 11:
    numeroJogador = input("Digite o número do jogador que será escalado: ")
    for jogadorParaEscalar in lst_jogadores:
      if jogadorParaEscalar.getNumero() == numeroJogador:
        lst_escalados.append(jogadorParaEscalar)
        print(f'Jogador {jogadorParaEscalar.getNomeJogador()} escalado!')


def opcao3():
  print('print R')

def opcao4():
  print('print R')

def opcao5():
  print('print R')

def init():
    resposta = input(message)

    if resposta == "1":
      opcao1()
    elif resposta == "2":
      opcao2()



while True:
  init()
