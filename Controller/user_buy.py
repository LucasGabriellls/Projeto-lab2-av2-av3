from tkinter import messagebox
import datetime


from Model.orders import DataBaseOrder
from Model.user_db import DataBaseUser
from Model.product_db import DataBaseProduct
from View.user_buy_screen import buy, cart_screen

class Buy:
    @staticmethod
    def check_product():
        from View.home import sign_in

        result = DataBaseProduct.select_product_buy()
        if result:
            try:
                buy(result)
            except Exception as e:
                messagebox.showerror('Erro', f'Erro ao entrar na tela de compras. {e}')
        else:
            messagebox.showerror('Erro', 'Não existe nenhum produto cadastrado no momento.')
            sign_in()
    
    @staticmethod
    def list_filter(root, key_word_combox, key_word_entry):
        if key_word_entry:
            root.destroy()
            result = DataBaseProduct.list_name(key_word_entry)
            buy(result)
        else:
            if key_word_combox:
                if key_word_combox == 'Valor Crescente':
                    root.destroy()
                    result_asc = DataBaseProduct.rising_price()
                    buy(result_asc)
                elif key_word_combox == 'Valor Decrescente':
                    root.destroy()
                    result_desc = DataBaseProduct.decreasing_price()
                    buy(result_desc)
                elif key_word_combox == 'Ordem Alfabética':
                    root.destroy()
                    result_alph = DataBaseProduct.alphabetical_order()
                    buy(result_alph)
            else:
                messagebox.showinfo('Informação', 'Nenhum filtro Selecionado/Digitado.')
                root.destroy()
                buy()

    @staticmethod
    def new_order(email):
        global id_order

        try:
            date_today = datetime.date.today()
            get_id = DataBaseUser.get_id(email)
            id_order = DataBaseOrder.insert_order(get_id, str(date_today), 'Pendente')
        except Exception as e:
            messagebox.showerror('Erro', f'Erro ao inserir um novo pedido. {e}')

    @staticmethod
    def check_buy(id_product, amount, payment= None):
        global qnt_prod
        global id_prod

        id_prod = id_product
        result_id = DataBaseProduct.id_product_search(id_product)
        if result_id:
            payment = ''
            qnt_prod = DataBaseOrder.order(amount, id_product, id_order)
            messagebox.showinfo('Informação', 'Produto adicionado com sucesso.')
        else:
            messagebox.showerror('Erro', 'Não existe nenhum produto com esse ID.')
    
    @staticmethod
    def cart_market(root):
       # get_id = DataBaseOrder.list_id(id_order= id_order)
        #if get_id:
            root.destroy()
            get_id = DataBaseOrder.get_orders(id_order)
            cart_screen(get_id)
        #else:
            #messagebox.showinfo('Informação', 'Nenhum produto selecionado.')

    @staticmethod
    def quit_buy(root):
        from View.home import sign_in


        DataBaseOrder.quit(id_order= id_order)
        root.destroy()
        sign_in()

    @staticmethod   
    def payment(root, payment_method, address, nation, cep, phone, cpf):
        from View.home import sign_in


        if payment_method and address and nation and cep and phone and cpf:
            id_user = DataBaseOrder.select_id_user(id_order)
            DataBaseUser.update_user(id= id_user, address= address, nation= nation, cep= cep, phone= phone, cpf= cpf)
            DataBaseOrder.order_payment(id= id_order, payment_method= payment_method, status= 'APROVADO')
            messagebox.showinfo('Informação', 'Pedido realizado com sucesso.')   
            DataBaseOrder.delete_stock_db(id_prod= id_prod, qndt= qnt_prod)
            root.destroy() 
            sign_in()    
        else:
            messagebox.showerror('ERRO', 'Digite todas as informações pedidas.')

