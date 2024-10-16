from random import randint
import os

produtos = list()

#\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/#
    
def adicionar_prod():
    os.system('cls')
    print('=' * 50)
    print('ADICIONAR PRODUTO')
    add_prod = input('Nome do Produto: ')

    if len(produtos) == 0:
        estoque = {'produto' : add_prod, 'estoque' : 0, 'id_produto' : randint(0, 100)}
        produtos.append(estoque.copy())
        print('Produto Adicionado com Sucesso')
        os.system('pause')
        os.system('cls')
        return
    else:
        for i in produtos:
            if add_prod == i['produto']:
                print('Este Produto já Existe...')
                print('Retornando ao Menu...')
                os.system('pause')
                os.system('cls')
                return
        estoque = {'produto' : add_prod, 'estoque' : 0, 'id_produto' : randint(0, 100)}
        produtos.append(estoque.copy())
        print('Produto Adicionado com Sucesso')
        os.system('pause')
        os.system('cls')
        return

#\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/#

def listar_produtos():
    os.system('cls')
    print('=' * 50)
    print('PRODUTOS CADASTRADOS')
    print('=' * 50)
    
    if len(produtos) == 0:
        print('Não Existe Nenhum Produto Cadastro...')
        print('=' * 50)
        os.system('pause')
        os.system('cls')
    else:
        for i in produtos:
            print(f'Nome: {i['produto']} | Estoque: {i['estoque']} | id: {i['id_produto']}')

        print('=' * 50)
        os.system('pause')
        os.system('cls')

#\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/#

def estoque_prod():
    os.system('cls')
    print('=' * 50)
    print('ADICIONAR ESTOQUE')
    print('=' * 50)
    
    try:
        prod_estq = int(input('Id do Produto: '))
        qnt_estq = int(input('Quantidade Adicional Para o Estoque: '))

        if qnt_estq < 1:
            print('Insira Um Valor Maior Que 1...')
        
        else:
            for i in produtos:
                if prod_estq == i['id_produto']:
                    i['estoque'] += qnt_estq
                    print('Estoque Atualizado...')
                    os.system('pause')
                    return 
                
            print('Produto Não Encontrado....')
            os.system('pause')
        
    except ValueError:
        print('Digite o Valor Inteiro do Produto.')
        os.system('pause')

#\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/#

def remover_produto():
    os.system('cls')
    print('=' * 50)
    print('REMOVER PRODUTO')
    print('=' * 50)

    try:
        prod_rm = int(input('Id do Produto: '))
        
        for i in range(len(produtos)):
            if prod_rm == produtos[i]['id_produto']:
                del produtos[i]
                print('Produto Removido...')
                os.system('pause')
                return

        print('Produto Não Encontrado...')
        os.system('pause')

    except ValueError:
        print('Digite o Valor Inteiro do Produto.')
        os.system('pause')

#\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/#