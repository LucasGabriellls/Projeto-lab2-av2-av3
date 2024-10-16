from produto import *
from cliente import *
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
    print('BEM VINDO À ÁREA DE ADM!')
    print('=' * 50)
    print('LOGIN ')
    username_adm = input('Digite o nome de usuário: ')
    access_key_adm = input('Digite a senha: ')

    if user_adm == username_adm and key_adm == access_key_adm:
        menu_adm()
        return
    else:
        print('ADM NÃO ENCONTRADO')
        os.system('pause')
        os.system('cls')
        return

#\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/#

def menu_adm():
    while True:
        os.system('cls')
        print('=' * 50)
        print('Listar Produtos[LP] - Listar Vendas[LV] - Adicionar Produtos[AP] - Listar Cliente[LC] - Estoque Produto[EP] - Remover Produto[RM] - Sair[S]')
        opc = input('Sua Escolha: ').upper()

        if opc == 'LP':
            listar_produtos()
        
        elif opc == 'LV':
            print('Função em andamento')
            ...#list_venda()
            return
        
        elif opc == 'AP':
            adicionar_prod()

        elif opc == 'LC':
            listar_cliente()

        elif opc == 'EP':
            estoque_prod()
        
        elif opc == 'RM':
            remover_produto()
        
        elif opc == 'S':
            print('Voltando Para o Menu Principal...')
            os.system('pause')
            os.system('cls')
            return
        
        else:
            print('Opção inválida...')
            os.system('pause')
            os.system('cls')
            menu_adm()
            return

#\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/#