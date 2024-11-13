from tkinter import messagebox
import pyotp
import qrcode

from View.adm_screen import *


def auth():
        global totp
        key = pyotp.random_base32()
        uri = pyotp.totp.TOTP(key).provisioning_uri(issuer_name="Super Kernel")

        qrcode.make(uri).save("./View/imgs/totp.png")  
        totp = pyotp.TOTP(key)

class admin:
    def __init__(self, secret_key= None,  entry= None):
        self.entry = entry if entry else ""
        self.secret_key = secret_key

    def validate_entry(self, root):
        if self.entry != "":
            if totp.verify(str(self.entry)):
                print('ok')
            else:
                messagebox.showerror('Erro', 'Código errado, tente novamente')
        else:
            messagebox.showerror('Erro', 'Nenhum código foi digitado!')