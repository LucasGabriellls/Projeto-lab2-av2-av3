import os

#\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/#

def pix(total_pagar):
    os.system('cls')
    print('=' * 50)
    print('Chave Pix: (82) 9.9999-999')
    print('=' * 50)
    print(f'Total Pago: R${total_pagar}')
    print('Obrigado Pela Preferência!')
    os.system('pause')
    os.system('cls')
    return

#\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/#

def cartao_credito(total_pagar):
    os.system('cls')
    print('=' * 50)
    nmr = input('Número do Cartão: ')
    cvv = input('CVV: ')

    print(f'Total Pago: R${total_pagar}')
    print('Obrigado Pela Preferência!')
    os.system('pause')
    os.system('cls')
    return

#\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/#

def cartao_debito(total_pagar):
    os.system('cls')
    print('=' * 50)
    nmr = input('Número do Cartão: ')
    
    print(f'Total Pago: R${total_pagar}')
    print('Obrigado Pela Preferência!')
    os.system('pause')
    os.system('cls')
    return

#\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/#