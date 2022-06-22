# Avaliação 02 individual
# Autor: Gabriel Merigo

respostas_aceitas = ['1', '2', '3', '4']
login = []
senha = []
funcionarios = ['Pedro' , 'Ana', 'Carlos', 'Maria Clara', 'João Antonio']
salarios = [3470.00, 2200.00, 3970.34, 7450.23, 5677.33]

'''MÉTODOS'''
def verificarUsuario(usuarioDigitado):
    if not usuarioDigitado in login: raise ValueError('O usuário que você digitou não existe na lista de usuarios') 

def verificarSenha(senhaDigitada):
    if not senhaDigitada in senha: raise ValueError('A senha que você digitou está incorreta')

def formatarMensagemErro(string):
    string = string.replace('(', '')
    string = string.replace(')', '')
    string = string.replace("'", '')
    string = string.replace(',', '')
    return string

def retornarMensagemErro(ex):
    print(formatarMensagemErro(ex.args.__str__()))


def calcularMedia():
    return round(sum(salarios) / salarios.__len__(), 2)


'''ROTINAS DO USUÁRIO'''
def cadastroLoginSenha():
    usuario = input('Por favor, digite um nome de usuário para ser cadastrado: ')

    try:
        if usuario in login: raise ValueError(f'O usuário {usuario} já existe na lista de login, por favor digite outro nome')
        if not usuario in funcionarios: raise ValueError(f'O usuário {usuario} não existe na lista de funcionarios, por favor crie clicando [4]')

        login.append(usuario)
        senhaDigitada = input('Por favor, digite um senha para seu usuário: ')
        senha.append(senhaDigitada) 
        print('Usuário cadastrado com sucesso!')
    except ValueError as ex:
        retornarMensagemErro(ex)

def aumentarSalario():
    try:
        usuarioDigitado = input('Digite o nome de seu usuário: ')
        senhaDigitada = input(f'{usuarioDigitado}, digite a sua senha: ')
        verificarUsuario(usuarioDigitado)
        verificarSenha(senhaDigitada)
        media = calcularMedia()

        for i in range(salarios.__len__()):
            if salarios[i] < media:
                salarios[i] = round(salarios[i] + (salarios[i] * 0.10), 2)

        print('O aumento de 10% nos salários dos funcionarios abaixo da media foi realizado com sucesso!')
    except ValueError as ex:
        retornarMensagemErro(ex)

def gerarRelatorio():
    try:
        usuarioDigitado = input('Digite o nome de seu usuário: ')
        senhaDigitada = input(f'{usuarioDigitado}, digite a sua senha: ')
        verificarUsuario(usuarioDigitado)
        verificarSenha(senhaDigitada)
        for i in range(funcionarios.__len__()):
            print(f'{funcionarios[i]} - {salarios[i]}')
    except ValueError as ex:
        retornarMensagemErro(ex)

def criacaoNovoFuncionario():
    nomeFuncionario = input('Digite o nome do novo funcionario: ')
    try: 
        salarioFuncionario = float(input('Digite o salário do novo funcionario: '))
        funcionarios.append(nomeFuncionario)
        salarios.append(salarioFuncionario)
        print('Funcionário cadastrado com sucesso!')
    except:
        print('Ops... algo aconteceu de errado! Verifique se você realmente está digitando número.')

while True:
    message = '''\n MENU - Você pode escrever "sair" para sair do menu \n 1 - Cadastrar Login e Senha \n 2 - Aumento de 10% \n 3 - Relatório \n 4 - Cadastrar Funcionário \n Escolha: '''
    escolha = input(message)


    if str(escolha).lower() == 'sair': break
    
    try: 
      if not escolha in respostas_aceitas: raise ValueError('Você só pode digitar 1, 2, 3 e 4')
    except ValueError as ex:
      retornarMensagemErro(ex)
      continue
    
    if escolha == '1':
        cadastroLoginSenha()
    elif escolha == '2':
        aumentarSalario()
    elif escolha == '3':
        gerarRelatorio()
    elif escolha == '4':
        criacaoNovoFuncionario()

print('Você saiu do loop')