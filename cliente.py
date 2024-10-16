import os

lista_usuarios = list()

#\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/#

def inserir(user, key, id):
    dicionario_usuario = {'username' : user, 'password' : key, 'id' : id}
    '''
        A 'lista_usuarios' recebe uma cópia do meu dicionário, ou seja, após os dados recebidos
        pelo usuário no dicionário, eles serão copiados para a minha lista, 
        ex: lista_usuarios[{'username' : 'Lucas', 'password' : '12345', 'id' : id}]
    '''
    lista_usuarios.append(dicionario_usuario.copy()) 
    print('Usuário Cadastrado com Sucesso...')
    os.system('pause')
    os.system('cls')

#\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/#


def listar_cliente():
    os.system('cls')
    print('=' * 50)
    print('CLIENTES CADASTRADOS')
    print('=' * 50)
    for i in lista_usuarios:
        print(f'Nome: {i['username']} | id: {i['id']}')

    print('=' * 50)
    os.system('pause')
    os.system('cls')
    
#\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/#