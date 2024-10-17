from cliente import *
from random import randint
from compra import *

#\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/#

def cadastrar_usuario():
    print('CRIE O USUÁRIO:')
    print('=' * 50)
    user = input('Nome de usuário: ')
    key = input('Senha: ')
    print('=' * 50)
    validar(user, key)

#\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/#

def validar(user, key):
    cont_id = randint(1, 100000) # Utilizando o método 'randint' para gerar números aleatórios para o id.
    if len(lista_usuarios) == 0: # Se minha lista estiver vazia ele vai inserir o usuário.
        inserir(user, key, cont_id) 
        menu_compra()
        
    else:

        for i in lista_usuarios: 
            if user == i['username']:  # Verificando se existe algum usuário igual.
                if key == i['password']: # Verificando se a senha inserida por usuários de mesmo 'nome' são iguais.
                    print('Senha existente...')
                    os.system('pause')
                    os.system('cls')
                    cadastrar_usuario()
                    return
                
        inserir(user, key, cont_id) 
        menu_compra()

#\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/#