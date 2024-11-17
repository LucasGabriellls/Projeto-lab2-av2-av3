from tkinter import messagebox
import pyotp
import qrcode

from View.adm_screen import admin_roles
from View.adm_product_screen import add_product_screen


class admin:
    def __init__(self, secret_key= None,  entry= None):
        self.entry = entry if entry else ""
        self.secret_key = secret_key

    def validate_entry(self, root):
        if self.entry != "":
            try:
                if totp.verify((self.entry)):
                    root.destroy()
                    admin_roles()
                else:
                    messagebox.showerror('Erro', 'Código errado, tente novamente')
            except Exception as e:
                messagebox.showerror('Erro', f'ERRO: {e}')
        else:
            messagebox.showerror('Erro', 'Nenhum código foi digitado!')
    
    def add_product(self, root, name_product, price, category, new_category, description= None, qnt_stock = None):
        ...
        

def auth():
        global totp
        key = pyotp.random_base32()
        uri = pyotp.totp.TOTP(key).provisioning_uri(name='Admin Login', issuer_name='Super Kernel')

        qrcode.make(uri).save("./View/imgs/totp.png")  
        totp = pyotp.TOTP(key)