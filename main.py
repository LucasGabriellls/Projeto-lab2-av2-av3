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

        elif opc == 'L':
            os.system('cls')
            login()

        elif opc == 'S':
            os.system('cls')
            print('=' * 50)
            print('PROGRAMA ENCERRADO...')
            print('Volte Sempre!')
            print('=' * 50)
            return
        
        elif opc == 'ADM':
            adm()
            
        else:
            os.system('cls')
            print('Valor incorreto...Tente novamente')
            menu()

#\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/#

menu()