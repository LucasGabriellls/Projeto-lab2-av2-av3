import os

lista_usuarios = list()
dicionario_usuario = dict()

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