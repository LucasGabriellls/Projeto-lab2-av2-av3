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
            list_user(get_user)
        else:
            messagebox.showinfo('Informação', 'Ainda não possui usuários cadastrados.')
    
    @staticmethod
    def edit_user(root, id, name, address, nation, email):
        from Model.user_db import DataBaseUser
        from View.adm_screen import admin_roles

        user = DataBaseUser.select_user()
        if user:
            if id and name and address and nation and email:
                id_user = DataBaseUser.valid_id(id)
                try:
                    DataBaseUser.edit_user(name= name, address= address, nation= nation, email= email, id= id)
                    messagebox.showinfo('Informação', 'Usuário editado com sucesso.')
                except Exception as e:
                    messagebox.showerror('Erro', f'Erro ao editar usuário: {e}')
            else:
                messagebox.showerror('Erro', 'Digite todas informações pedidas.')
        else:
            messagebox.showinfo('Informação', 'Ainda não possui usuários cadastrados.')
            root.destroy()
            admin_roles()