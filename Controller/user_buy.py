from tkinter import messagebox


from Model.product_db import DataBaseProduct
from View.user_buy_screen import buy

class Buy:
    
    @staticmethod
    def check_product():
        from View.home import sign_in

        result = DataBaseProduct.search_product()
        #if result:
        try:
            buy()
        except Exception as e:
            messagebox.showerror('Erro', 'Erro ao entrar na tela de compras.')
        #else:
            #messagebox.showerror('Erro', 'Não existe nenhum produto cadastrado no momento.')
            #sign_in()
