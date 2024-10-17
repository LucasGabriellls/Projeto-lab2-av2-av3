from produto import *
from pagamento import *
import os

carrinho = list()
fim_compra = list()

#\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/#

def menu_compra():
    os.system('cls')
    print('=' * 50)
    print('Compra[c] - Sair[s]')
    opc = input('Sua Opção: ').upper()
    
    if opc == 'C':
        compra()
        
    elif opc == 'S':
        print('Retornando ao menu...')
        print('Volte Sempre.')
        os.system('pause')
        os.system('cls')
        return
    
    else:
        os.system('cls')
        print('Valor incorreto...Tente novamente')
        os.system('pause')
        os.system('cls')
        menu_compra()

#\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/#

def compra():
    produto_subtotal = dict()

    if len(produtos) > 0:
        os.system('cls')
        print('=' * 50)
        print('Bem Vindo ao Menu de Compras!')
        print('=' * 50)
        print('Produtos em Estoque: ') # Refatorar 3av, add um filtro de busca, onde o usuário pode digitar o nome do produto e ver se tem disponível.
        list_prod_compra()
        print()
        print('=' * 50)
        
        while True:
            try:
                id_buy = int(input('Digite o Id do Produto: '))
                print('=' * 50)

                for i in produtos:
                    if id_buy == i['id_produto']:
                        try:
                            qnt_buy = int(input('Quantidade:'))
                            if i['estoque'] >= qnt_buy:
                                produto_subtotal = {'nome_produto' : i['produto'] , 'valor_compra' : i['preco'], 'qnt_produto' : qnt_buy}
                                carrinho.append(produto_subtotal.copy())
                                os.system('cls')
                                print('=' * 50)
                                opc = input('Deseja Continuar Comprando? [S/N]').upper()
                                if opc == 'S':
                                    compra()
                                    break

                                elif opc == 'N':
                                    menu_pagamento()
                                    return
                                
                                else: 
                                    print('Valor Inserido Incorreto...')
                                    os.system('pause')
                                    os.system('cls')

                            else:
                                print('Quantidade no Estoque Insuficiente...') 
                                os.system('pause')
                                os.system('cls')
                            
                        except ValueError:
                            print('Digite Um Valor Inteiro Para a Quantidade da Compra...')
                            os.system('pause')
                            os.system('cls')

            except ValueError:
                print('Digite Um Valor Inteiro Para o ID do Produto...')
                os.system('pause')
                os.system('cls')

    else:
        print('Nenhum Produto Disponível..')
        os.system('pause')
        os.system('cls')
        return

#\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/#

def list_prod_compra():
         for i in produtos:
            if i['estoque'] > 0 and i['preco'] > 0:
                print(f'Nome: {i['produto']} | Estoque: {i['estoque']} | Valor: R${i['preco']} | ID: {i['id_produto']}')

#\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/#

def menu_pagamento():
    total_compra_fim = dict()
    total_compra = 0
    id_compra = randint(0, 100)

    os.system('cls')
    print('=' * 50)
    print('CARRINHO')
    print('=' * 50)
    print('Finalizar Compra[FC] - Cancelar Compra[CC] - Sair[S]')
    opc = input('Sua Opção: ').upper()

    if opc == 'FC':
        os.system('cls')
        print('=' * 50)

        for i in carrinho:
            print(f'Produto: {i['nome_produto']} | SubTotal: {i['valor_compra']} | Quantidade: {i['qnt_produto']}')
            total_compra += i['valor_compra'] * i['qnt_produto']
            
            if i['nome_produto'] in produtos:
                produtos[i]['estoque'] -= i['qnt_produto']

        print()
        print(f'Total: {total_compra} | ID-Compra: {id_compra}')
        print('=' * 50)

        print('PIX[P] - Cartão de Crédito[CC] - Cartão de Débito[CD]')
        forma_pagamento = input('Forma de Pagamento: ').upper()
        if forma_pagamento == 'P':
            total_compra_fim = {'valor_total' : total_compra, 'tipo_pagamento' : 'PIX', 'id_venda' : id_compra}
            fim_compra.append(total_compra_fim.copy)
            pix(total_compra)
            menu_compra()
        
        elif forma_pagamento == 'CC':
            total_compra_fim = {'valor_total' : total_compra, 'tipo_pagamento' : 'Cartao_credito', 'id_venda' : id_compra}
            fim_compra.append(total_compra_fim.copy)
            cartao_credito(total_compra)
            menu_compra()
        
        elif forma_pagamento == 'CD':
            total_compra_fim = {'valor_total' : total_compra, 'tipo_pagamento' : 'Cartao_Debito', 'id_venda' : id_compra}
            fim_compra.append(total_compra_fim.copy)
            cartao_debito(total_compra)
            menu_compra()
        
        else:
            print('Digite um Valor de Acordo com o Menu')
            os.system('pause')
            os.system('cls')

    elif opc == 'CC':
        print('Compra Cancelada')
        print('Volte Sempre')
        os.system('pause')
        os.system('cls')
        return
    
    elif opc == 'S':
        print('Retornando ao menu...')
        print('Volte Sempre.')
        os.system('pause')
        os.system('cls')
        return
    
    else:
        print('Você Deve Digitar um Valor de Acordo com o Menu.')
        os.system('pause')
        os.system('cls')
        menu_pagamento()

#\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/#

def listar_venda():
    os.system('cls')
    print('=' * 50)
    print('Lista De Vendas')
    print('=' * 50)
    for i in fim_compra:
        print(f'Valor: {i['valor_total']} | Forma de Pagamento: {i['tipo_pagamento']} | ID da Venda: {i['id_venda']}')