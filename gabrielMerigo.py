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