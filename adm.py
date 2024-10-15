from produto import *
import os

user_adm = 'adminMer' # senha de adm.
key_adm = 'admin123Mer'

'''
Isto deverá ficar aqui apenas nesta base do projeto, depois vamos tentar mudar
a forma que tratamos isso, como por ex o google autenticador que pode gerar
um token para o adm entrar
'''

#\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/#

def adm():
    os.system('cls')
    print('=' * 50)
    print('BEM VINDO A ABA DE ADM!')
    print('LOGIN: ')
    username_adm = input('Digite o nome de usuário: ')
    access_key_adm = input('Digite a senha: ')

    if user_adm == username_adm and key_adm == access_key_adm:
        menu_adm()
        return
    else:
        print('ADM NÃO ENCONTRADO')
        return

#\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/#

def menu_adm():
    os.system('cls')
    print('=' * 50)
    print('Listar Produtos[LP] - Listar Vendas[LV] - ADD Produtos[AP] - Listar Cliente[LC] - Estoque Produto[EP] - Remover Produto[RM] - Sair[S]')
    opc = input('Sua Escolha: ').upper()

    if opc == 'LP':
        print('Função em andamento')
        ...#list_prod()
        return
    elif opc == 'LV':
        ...#list_venda()
        return
    elif opc == 'AP':
        print('Função em andamento')
        os.system('pause')
        os.system('cls')
        #adicionar_prod()
        return
    elif opc == 'LC':
        print('Função em andamento')
        os.system('pause')
        os.system('cls')
        ...#list_client()
        return
    elif opc == 'EP':
        print('Função em andamento')
        os.system('pause')
        os.system('cls')
        ...#estq_prod()
        return
    elif opc == 'RM':
        print('Função em andamento')
        os.system('pause')
        os.system('cls')
        ...#remover_prod()
        return
    elif opc == 'S':
        print('Voltando Para o Menu Principal...')
        os.system('pause')
        os.system('cls')
        return
    else:
        print('Opção inválida...')
        menu_adm()
        return

#\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/#