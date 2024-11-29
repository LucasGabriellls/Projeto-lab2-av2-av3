from tkinter import messagebox
import pyotp
import qrcode

from View.adm_screen import admin_roles
from View.adm_product_screen import remove_product_screen, edit_product_screen
from View.adm_user_screen import remove_user_screen, edit_user_screen
from Model.product_db import DataBaseProduct
from Model.user_db import DataBaseUser

class admin:
    def __init__(self, secret_key= None,  entry= None):
        self.entry = entry if entry else ""
        self.secret_key = secret_key

    def validate_entry(self, root):
        if self.entry != "":
            try:
                #if totp.verify((self.entry)):
                    root.destroy()
                    admin_roles()
                #else:
                    #messagebox.showerror('Erro', 'Código errado, tente novamente')
            except Exception as e:
                messagebox.showerror('Erro', f'ERRO autenticação: {e}')
        else:
            messagebox.showerror('Erro', 'Nenhum código foi digitado!')
    
    @staticmethod
    def add_product(root, name_product, price, category, new_category, description= None, qnt_stock = None):
        if name_product and price and (category or new_category) and description and qnt_stock:
            if category:
                if name_product and price:
                    try:
                        if qnt_stock == None:
                            result_stock = 0
                        else:
                            result_stock = admin.check_stock(stock_c= int(qnt_stock))
                        result_price = admin.check_price(price_c= float(price))
                        category_id = admin.select_id_category(search_category_id= category)
                        DataBaseProduct.add_product(name= name_product, stock= result_stock, price_p= price, category_id_p= category_id, description_c= description)
                        root.destroy()
                        admin_roles()
                    except Exception as e:
                        messagebox.showerror('ERRO', 'Erro: Tentativa de adicionar novo produto, falha.')
                else:
                    messagebox.showerror('ERRO','Digite o Nome e o Preço do produto.')
            elif new_category:
                if name_product and price:
                    try:
                        
                        if qnt_stock == None:
                            result_stock = 0
                        else:
                            result_stock = admin.check_stock(stock_c= int(qnt_stock))
                        result_price = admin.check_price(price_c= float(price))
                        result_search = admin.find_equal_category(search_category= new_category)

                        if result_search:
                            messagebox.showinfo('INFORMAÇÃO', 'Já possui uma categoria com esse nome')
                        else:
                            DataBaseProduct.add_category(category_c= new_category)
                            category_id = admin.select_id_category(new_category)
                            DataBaseProduct.add_product(name= name_product, stock= result_stock, price_p= result_price, category_id_p= category_id, description_c= description)
                            root.destroy()
                            admin_roles()
                    except Exception as e:
                        messagebox.showerror('ERRO', f'ERRO categoria: {e}')
                else:
                    messagebox.showerror('ERRO', 'Erro: Tentativa de adicionar novo produto, falha.')
            else:
                messagebox.showerror('Erro', 'Nenhuma categoria selecionada/criada.')
        else:
            messagebox.showerror('Erro', 'Digite todas as informações pedidas')

    @staticmethod
    def categories():
        result = DataBaseProduct.select_category()
        if result:
            return result
        else:
            return ''
    
    @staticmethod
    def select_id_category(search_category_id):
        try:
            return DataBaseProduct.search_id_category(category= search_category_id)
        except Exception as e:
            messagebox.showerror('ERRO', 'Erro ao procurar o id_categoria')

    @staticmethod
    def find_equal_category(search_category):
        result_select = DataBaseProduct.equal_category(name_category= search_category)

        if result_select:
            return True
        else:
            return False
    
    @staticmethod
    def check_stock(stock_c):
        value = stock_c
        if value >= 0:
            return value
        else:
            value = 0
            return value
    
    @staticmethod
    def check_price(price_c):
        if price_c >= 0:
            return price_c
        else:
            price_c = 0.0
            return price_c  
    
    @staticmethod
    def info_remove_product(root):
        result = DataBaseProduct.select_product_all()
        if result:
            root.destroy()
            remove_product_screen()
        else:
            messagebox.showerror('ERRO', 'Não existe nenhum produto cadastrado no momento.')
            root.destroy()
            admin_roles()
    
    @staticmethod
    def info_edit_product(root):
        result = DataBaseProduct.select_product_all()
        if result:
            root.destroy()
            edit_product_screen()
        else:
            messagebox.showerror('ERRO', 'Não existe nenhum produto cadastrado no momento.')
            root.destroy()
            admin_roles()
    
    @staticmethod
    def info_remove_user(root):
        result = DataBaseUser.select_user()
        if result:
            root.destroy()
            remove_user_screen()
        else:
            messagebox.showerror('ERRO', 'Não existe nenhum produto cadastrado no momento.')
            root.destroy()
            admin_roles()
    
    @staticmethod
    def info_edit_user(root):
        result = DataBaseUser.select_user()
        if result:
            root.destroy()
            edit_user_screen()
        else:
            messagebox.showerror('ERRO', 'Não existe nenhum produto cadastrado no momento.')
            root.destroy()
            admin_roles()

def auth():
        global totp
        key = pyotp.random_base32()
        uri = pyotp.totp.TOTP(key).provisioning_uri(name='Admin Login', issuer_name='Super Kernel')

        qrcode.make(uri).save("./View/imgs/totp.png")  
        totp = pyotp.TOTP(key)