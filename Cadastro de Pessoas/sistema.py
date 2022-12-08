from ProjetoAdmtec.library.Interface import *
from ProjetoAdmtec.library.Arquivo import *
from time import sleep

arq = 'ProjetofinalAdmtec.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Ver Clientes Cadastrados', 'Cadastrar Novo Cliente', 'Sair do Sistema'])
    if resposta == 1:
        # Opção de listar o conteúdo de um arquivo!
        lerArquivo(arq)
    elif resposta == 2:
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        # Opção de sair do sistema.
        cabeçalho('Saindo do Sistema.')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida!\033[m')
    sleep(2)
