from tkinter import messagebox
from Model.market_db import DataBase
import bcrypt


class User:
    def __init__(self, name = None, email = None, password = None):
        self.name = name
        self.email = email
        self.password = password

    def validate_record(result, root):
        from View.home import sign_in

        void_box = User.validate_entry_record(result)
        if void_box == True:
            user = DataBase.record_list_user(result.email)
            if user:
                messagebox.showinfo('Informação', 'Já existe usuário com esse email')
            else:
                root.destroy()
                User.insert_new_user(result)
                sign_in()
        else:
            messagebox.showinfo('Informação', 'É necessário digitar NOME, EMAIL E SENHA!')

    def validate_entry_record(result):
        if result.email and result.name and result.password:
            return True
        else:
            return False
    
    def Encrypt_password(result):
        try:
            password = result.password

            password_bytes = password.encode('utf-8')
            salt = bcrypt.gensalt()
            hashed = bcrypt.hashpw(password_bytes, salt)
            return hashed
        except Exception as e:
           messagebox.showerror('ERRO', 'Criptografia mal-sucedida!')
    
    def insert_new_user(result):
        try:
            name = result.name
            email = result.email
            password = User.Encrypt_password(result)

            DataBase.insert_user(name= name, email= email, password= password)
            messagebox.showinfo('Informação', 'Seu cadastro foi realizado com sucesso!')

        except Exception as e:
            messagebox.showerror('ERRO', 'Erro ao cadastrar usuário!')


    def validate_sign_in(result, root):
        from View.home import adm_sign_in

        adm_password = 'admin123mer'

        box_void = User.validate_entry_login(result)
        if box_void:
            if result.email == adm_password and result.password == adm_password:
                root.destroy()
                adm_sign_in()
            else:
                result_select = DataBase.login_list_user(result.email)

                if result_select:
                    try:
                        email, password = result_select
                        password_validate = User.validate_password(result, password)
                        if password_validate:
                            root.destroy()
                            #buy()
                        else:
                            messagebox.showinfo('Informação', 'Nenhum usuário encontradosss!')

                    except Exception as e:
                        messagebox.showerror('Erro', 'Erro ao verificar login!')
                        
                else:
                    messagebox.showinfo('Informação', 'Nenhum usuário encontrado')
        else:
            messagebox.showinfo('Informação', 'É necessário digitar EMAIL E SENHA!')
        
    def validate_entry_login(result):
        if result.email and result.password:
            return True
        else:
            return False  

    def validate_password(result, password_hash):
            try:
                print(result.password)
                password_bytes = result.password.encode('utf-8') 
                print(type(result.password))
                password_hash = password_hash.tobytes() 
                print(password_hash)
                print(password_bytes)
                return bcrypt.checkpw(password_bytes, password_hash)
            
            except Exception as e:
                messagebox.showerror('Erro', 'Eror ao validar senha!')
                return None