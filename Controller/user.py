from tkinter import messagebox
import bcrypt

from Model.market_db import DataBase
from Controller.adm import admin, auth


class User:
    def __init__(self, name = None, email = None, password = None):
        self.name = name
        self.email = email
        self.password = password

    def validate_record(self, root):
        from View.home import sign_in

        void_box = User.validate_entry_record(self)
        if void_box == True:
            user = DataBase.record_list_user(self.email)
            if user:
                messagebox.showinfo('Informação', 'Já existe usuário com esse email')
            else:
                root.destroy()
                User.insert_new_user(self)
                sign_in()
        else:
            messagebox.showinfo('Informação', 'É necessário digitar NOME, EMAIL E SENHA!')

    def validate_entry_record(self):
        if self.email and self.name and self.password:
            return True
        else:
            return False
    
    def Encrypt_password(self):
        try:
            password = self.password

            password_bytes = password.encode('utf-8')
            salt = bcrypt.gensalt()
            hashed = bcrypt.hashpw(password_bytes, salt)
            return hashed
        except Exception as e:
           messagebox.showerror('ERRO', 'Criptografia mal-sucedida!')
    
    def insert_new_user(self):
        try:
            name = self.name
            email = self.email
            password = User.Encrypt_password(self)

            DataBase.insert_user(name= name, email= email, password= password)
            messagebox.showinfo('Informação', 'Seu cadastro foi realizado com sucesso!')

        except Exception as e:
            messagebox.showerror('ERRO', 'Erro ao cadastrar usuário!')


    def validate_sign_in(self, root):
        from View.home import adm_sign_in

        adm_password = 'admin123mer'

        box_void = User.validate_entry_login(self)
        if box_void:
            if self.email == adm_password and self.password == adm_password:
                root.destroy()
                auth()
                adm_sign_in()
            else:
                result_select = DataBase.login_list_user(self.email)

                if result_select:
                    try:
                        email, password = result_select
                        password_validate = User.validate_password(self, password)
                        if password_validate:
                            root.destroy()
                            #buy()
                        else:
                            messagebox.showinfo('Informação', 'Nenhum usuário encontrado!')

                    except Exception as e:
                        messagebox.showerror('Erro', 'Erro ao verificar login!')
                        
                else:
                    messagebox.showinfo('Informação', 'Nenhum usuário encontrado')
        else:
            messagebox.showinfo('Informação', 'É necessário digitar EMAIL E SENHA!')
        
    def validate_entry_login(self):
        if self.email and self.password:
            return True
        else:
            return False  

    def validate_password(self, password_hash):
            try:
                print(self.password)
                password_bytes = self.password.encode('utf-8') 
                print(type(self.password))
                password_hash = password_hash.tobytes() 
                print(password_hash)
                print(password_bytes)
                return bcrypt.checkpw(password_bytes, password_hash)
            
            except Exception as e:
                messagebox.showerror('Erro', 'Erro ao validar senha!')
                return None