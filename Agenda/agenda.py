import requests
from tkinter import *

def cadastrarContato():

    idContato = input("Escolha o Id do seu contato: ")
    nome = input("Escreva o nome do seu contato: ")
    telefone = input("Escreva o numero de telefone do seu contato: ")
    email = input("Escreva o email do seu contato: ")
    try:
        agenda = open("agenda.txt", "a")
        dados = f'{idContato};{nome};{telefone};{email}\n'
        agenda.write(dados)
        agenda.close()
        print(f'Contato gravado com sucesso!!!')
    except:
        print("ERRO na gravação do contato")

def listarContato():
            agenda = open("agenda.txt", "r")
            for contato in agenda:
                print(contato)
            agenda.close()

def deletarContato():
    nomeDeletado = input("Digite o nome para ser deletado: ")
    agenda = open("agenda.txt","r")
    aux = []
    aux2 = []
    for i in agenda:
        aux.append(i)
    for i in range(0, len(aux)):
         if nomeDeletado not in aux[i]:
            aux2.append(aux[i])
            agenda = open("agenda.txt","w")
    for i in aux2:
            agenda.write(i)
            print(f'Contato deletado com sucesso')
            listarContato()
            agenda.close()

def buscarContatoPeloNome():
    nome = input(f'digite o nome a ser procurado: ')
    agenda = open("agenda.txt","r")
    for contato in agenda:
        if nome in contato.split(";")[1]:
            print(contato)
    agenda.close()

def sair():
    print(f'Ate mais... !!!')
    exit()

def main():

 main()




janela = Tk()
janela.title("AGENDA")

texto_orientacao = Label(janela, text="AGENDA")
texto_orientacao.grid(column=3, row=1)

texto_orientacao = Label(janela, text="AGENDA TELEFONICA")
texto_orientacao.grid(column=3, row=2)

texto_orientacao = Label(janela, text="CADASTRAR")
texto_orientacao.grid(column=1, row=3)

botao = Button(janela, text="CADASTRAR", command=cadastrarContato)
botao.grid(column=1, row=3)

texto_orientacao = Label(janela, text="LISTAR")
texto_orientacao.grid(column=2, row=3)

botao = Button(janela, text="LISTAR", command=listarContato)
botao.grid(column=2, row=3)


texto_orientacao = Label(janela, text="DELETAR")
texto_orientacao.grid(column=3, row=3)

botao = Button(janela, text="DELETAR", command=deletarContato)
botao.grid(column=3, row=3)

texto_orientacao = Label(janela, text="BUSCAR")
texto_orientacao.grid(column=4, row=3)

botao = Button(janela, text="BUSCAR", command=buscarContatoPeloNome)
botao.grid(column=4, row=3)

texto_orientacao = Label(janela, text="SAIR")
texto_orientacao.grid(column=5, row=3)

botao = Button(janela, text="SAIR", command=SystemExit)
botao.grid(column=5, row=3)


janela.mainloop()



def menu():
    opcao = input('''
==================================================
 MENU:

 [1]CADASTRAR CONTATO
 [2]LISTAR CONTATO
 [3]DELETAR CONTATO
 [4]BUSCAR CONTATO PELO NOME
 [5]SAIR
==================================================
ESCOLHA UMA OPÇÃO ACIMA: 
''')
    if opcao == "1":
        cadastrarContato()
    elif opcao == "2":
        listarContato()
    elif opcao == "3":
        deletarContato()
    elif opcao == "4":
        buscarContatoPeloNome()
    else:
        sair()
def cadastrarContato():

    idContato = input("Escolha o Id do seu contato: ")
    nome = input("Escreva o nome do seu contato: ")
    telefone = input("Escreva o numero de telefone do seu contato: ")
    email = input("Escreva o email do seu contato: ")
    try:
        agenda = open("agenda.txt", "a")
        dados = f'{idContato};{nome};{telefone};{email}\n'
        agenda.write(dados)
        agenda.close()
        print(f'Contato gravado com sucesso!!!')
    except:
        print("ERRO na gravação do contato")


def listarContato():
    agenda = open("agenda.txt", "r")
    for contato in agenda:
      print(contato)
    agenda.close()


def deletarContato():
    nomeDeletado = input("Digite o nome para ser deletado: ")
    agenda = open("agenda.txt","r")
    aux = []
    aux2 = []
    for i in agenda:
        aux.append(i)
    for i in range(0, len(aux)):
         if nomeDeletado not in aux[i]:
            aux2.append(aux[i])
            agenda = open("agenda.txt","w")
    for i in aux2:
            agenda.write(i)
            print(f'Contato deletado com sucesso')
            listarContato()
            agenda.close()



def buscarContatoPeloNome():
    nome = input(f'digite o nome a ser procurado: ')
    agenda = open("agenda.txt","r")
    for contato in agenda:
        if nome in contato.split(";")[1]:
            print(contato)
    agenda.close()

def sair():
    print(f'Ate mais... !!!')
    exit()

def main():

  menu()


main()