import numpy as np 

primeira_faixa = []
segunda_faixa = []
terceira_faixa = []

'''ROTINAS'''
def criar_mensagem(nomeFaixa, qntdIdadesNaFaixa):
    if qntdIdadesNaFaixa.__len__() == 0:
        mensagem = f'{nomeFaixa} não houve alunos digitados \n'
    else:
        mensagem = f'{nomeFaixa} é {max(qntdIdadesNaFaixa)} anos \n'
    return mensagem
    
def verificarMediaTurma(media):
    if media <= 25 : return 'Jovem'
    if media >= 26 and media <= 60 : return 'Adulta'
    if media >= 61 : return 'Idosa'

def calculaMediaERetornaMensagem(qntdAlunos): 
    media = sum(qntdAlunos) / int(qntdAlunos.__len__())

    print(
        f'- A média de idades da Turma é: {media}\n',
        f'- Portanto, pode-se dizer que a turma é {verificarMediaTurma(media)}\n', 
        'Para essa turma a maior idade digitada para a: \n',
        criar_mensagem('primeira faixa', primeira_faixa),
        criar_mensagem('segunda faixa', segunda_faixa),
        criar_mensagem('terceira faixa', terceira_faixa)
    )

def concatArrays():
    return np.concatenate((primeira_faixa, segunda_faixa, terceira_faixa))

'''Lógica para criação do algoritmo'''
while concatArrays().__len__() <= 41:
    valorDigitado = input('Digite a idade do aluno ou digite "fim" para sair: ')
    qntdAlunos = concatArrays()

    if str(valorDigitado).lower() == 'fim':
        if qntdAlunos.__len__() == 0: 
            print('Você finalizou o processo sem digitar nenhuma idade...') 
            break
        calculaMediaERetornaMensagem(qntdAlunos)
        break

    try:
        idade = int(valorDigitado)
    except:
        print('Ops... algo aconteceu de errado! Verifique se você realmente está digitando número.')
        continue
    
    if idade >= 0 and idade <= 25:
        primeira_faixa.append(idade)
    elif idade >= 26 and idade <= 60:
        segunda_faixa.append(idade)
    else:
        terceira_faixa.append(idade)

calculaMediaERetornaMensagem(qntdAlunos)

''' ------ '''
lista_Profissionais = []
lista_visitantes = []
lista_visitas = []


class Profissional:
    def __init__(self, nome, especialidade, sala):
        self.__nome = nome
        self.__especialidade = especialidade
        self.__sala = sala

    def getNome(self):
        return f'{self.__nome}'

    def getEspecialidade(self):
        return f'{self.__especialidade}'

    def getSala(self):
        return f'{self.__sala}'


class Visitante:
    def __init__(self, nome, documento):
        self.__nome = nome
        self.__documento = documento

    def getNome(self):
        return f'{self.__nome}'

    def getDocumento(self):
        return f'{self.__nome}'


class Visita:
    def __init__(self, visitante, profissional, data):
        self.__visitante = visitante
        self.__profissional = profissional
        self.__data = data

    def getVisitante(self):
        return f'{self.__visitante}'

    def getProfissional(self):
        return f'{self.__profissional}'

    def getData(self):
        return f'{self.__data}'


def cadastrarProfissional():
    nomeProfissional = input('Digite o nome do profissional: ')
    especialidadeProfissional = input(
        'Digite a especialidade do profissional: ')
    salaProfissional = input('Digite a sala do profissional: ')

    profissional = Profissional(
        nomeProfissional, especialidadeProfissional, salaProfissional)
    lista_Profissionais.append(profissional)

    print("Seu profissional foi cadastrado!")


def buscarProfissional(nome):
    for profissional in lista_Profissionais:
        if profissional.getNome() == nome:
            print(
                f"O profissional em questão é {profissional.getNome()} - a sala é {profissional.getSala()} - e sua especialidade {profissional.getEspecialidade()}")
        else:
            print("Profissional não encontrado!")


def cadastrarVisitante():
    nomeVisitante = input('Digite o nome do visitante: ')
    documento = input('Digite o documento: ')
    visitante = Visitante(nomeVisitante, documento)
    lista_visitantes.append(visitante)


def buscaVisitanteProfissionalECadastraData():
    nomeVisitante = input('Digite o nome do visitante: ')
    nomeProfissional = input('Digite o nome do Profissional: ')

    for visitante in lista_visitantes:
        if visitante.getNome() == nomeVisitante:
            print(f"O visitante é o {visitante.getNome()}")
            for profissional in lista_Profissionais:
                if profissional.getNome() == nomeProfissional:
                    print(
                        f"O profissional em questão é {profissional.getNome()}")
                    data = input("Digite a data da visita: ")
                    visita = Visita(nomeVisitante, nomeProfissional, data)

                    lista_visitas.append(visita)
                    print(f"Visita cadastrada!")
                else:
                    print("O profissional não foi encontrado")
        else:
            print("O visitante não foi encontrado")


def relatorio():
    for visita in lista_visitas:
        print(
            f"Profissional: {visita.getProfissional()} - Visitante: {visita.getVisitante()} - Data: {visita.getData()}")


def init():
    escolha = input('1- Cadastrar Profissional \n' +
                    '2- Localizar Profissional \n' +
                    '3- Cadastrar Visitante \n' +
                    '4- Registrar Visita \n' +
                    '5- Relatório de Conferência \n' +
                    'Escolha: '
                    )

    match escolha:
        case "1":
            cadastrarProfissional()
        case "2":
            nomeAtualProfissional = input(
                'Qual seria o nome do profissional? ')
            buscarProfissional(nomeAtualProfissional)
        case "3":
            cadastrarVisitante()
        case "4":
            buscaVisitanteProfissionalECadastraData()
        case "5":
            relatorio()


while True:
    init()
