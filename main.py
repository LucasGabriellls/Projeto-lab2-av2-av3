from cadastro import cadastrar_usuario
from login import login
from adm import adm
import os

#\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/#

def menu():
    while True:
        print('=' * 50)
        print('Cadastro[c] - Login[L] - Sair[S]')
        opc = input('Sua Escolha: ').upper()

        if opc == 'C':
            os.system('cls')
            cadastrar_usuario()
            return
        elif opc == 'L':
            os.system('cls')
            login()
            return
        elif opc == 'S':
            os.system('cls')
            print('PROGRAMA ENCERRADO...')
            print('Volte Sempre!')
            return
        elif opc == 'ADM':
            adm()
        else:
            os.system('cls')
            print('Valor incorreto...Tente novamente')
            menu()

#\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/#

menu()