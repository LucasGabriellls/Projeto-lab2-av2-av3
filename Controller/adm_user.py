from tkinter import messagebox


class AdminUser:
    
    @staticmethod
    def remove_user(id, name):
        from Model.user_db import DataBaseUser


        if id and name:
            get_id = DataBaseUser.valid_id(id= id)
            if get_id:
                try:
                    DataBaseUser.remove_user(id)
                    messagebox.showinfo('Informação', 'Usuário excluido com sucesso.')
                except Exception as e:
                    messagebox.showerror('Erro', f'Erro ao remover usuário: {e}')
            else:
                messagebox.showerror('Erro', 'Erro, não existe nenhum usuário com esse id;')
        else:
            messagebox.showerror('Erro', 'Digite todas as informações solicitadas.')
    
    @staticmethod
    def list_user(root):
        from Model.user_db import DataBaseUser
        from View.adm_user_screen import list_user


        get_user = DataBaseUser.get_user()
        if get_user:
            root.destroy()
            print(get_user)
            list_user(get_user)
        else:
            messagebox.showinfo('Informação', 'Ainda não possui usuário cadastrado.')
    
    @staticmethod
    def edit_user():
        ...