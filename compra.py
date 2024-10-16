from produto import *
import os

#\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/#

def menu_compra():
    print('=' * 50)
    print('Compra[c] - Sair[s]')
    opc = input('Sua Opção: ').upper()
    
    if opc == 'C':
        compra()
        
    elif opc == 's':
        print('Retornando ao menu...')
        print('Volte Sempre.')
        os.system('pause')
        os.system('cls')
        return

#\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/#

def compra():
    print('=' * 50)
    '''
    falta terminar
    '''