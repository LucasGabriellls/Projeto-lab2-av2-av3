from cliente import *
from compra import *

#\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/#

def login():
    os.system('cls')
    print('=' * 50)
    print('FAÇA O LOGIN: ')
    user = input('Digite o nome de usuário: ')
    key = input('Digite sua senha: ')
    validar_login(user, key)
    menu_compra()

#\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/#

def validar_login(user, key):
    if len(lista_usuarios) == 0:
        print('Nenhuma Conta Existente...Tente novamente')
        os.system('pause')
        os.system('cls')
        return
    
    else:
        for i in lista_usuarios:
            if user == i['username'] and key == i['password']:
                print('Seja Bem vindo!')
                os.system('pause')
                os.system('cls')
                return
            
        print('Nenhuma Conta Existente...Tente novamente')
        os.system('pause')
        os.system('cls')
        return
    
#\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/#