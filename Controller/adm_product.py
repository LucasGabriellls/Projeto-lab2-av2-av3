from tkinter import messagebox


class AdminProduct:

    @staticmethod
    def remove_product(id, name, root):
        from Model.product_db import DataBaseProduct
        from View.adm_screen import admin_roles

        if id and name:
            result_search = DataBaseProduct.id_product_search(id_product= id)
            if result_search:
                result = DataBaseProduct.remove_product(id_product= id)
                if result:
                    messagebox.showinfo('Informação', 'Produto excluido com sucesso.')
                    root.destroy()
                    admin_roles()
                else:
                    messagebox.showerror('Erro', 'Não conseguimos remover o produto.')
                    root.destroy()
                    admin_roles()
            else:
                messagebox.showinfo('INFORMAÇÃO', 'Nenhum produto cadastrado com esse ID.')
                root.destroy()
                admin_roles()
        else:
            messagebox.showerror('Erro', 'Digite todas informações pedidas.')
        
    
    @staticmethod
    def edit_product(id, name, stock, price, description, root):
        from Model.product_db import DataBaseProduct
        from View.adm_screen import admin_roles


        if id and name and stock and price and description:
            result_search = DataBaseProduct.id_product_search(id_product= id)
            if result_search:
                result = DataBaseProduct.edit_product(id_product= id, name_product= name, stock_product= stock, price_product= price, description_product= description)
                if result:
                    messagebox.showinfo('Informação', 'Produto editado com sucesso.')
                    root.destroy()
                    admin_roles()
                else:
                    messagebox.showerror('Erro', 'Não conseguimos editar o produto.')
                    root.destroy()
                    admin_roles()
            else:
                messagebox.showinfo('INFORMAÇÃO', 'Nenhum produto cadastrado com esse ID.')
                root.destroy()
                admin_roles()
        else:
            messagebox.showerror('Erro', 'Digites todas informações pedidas')

    @staticmethod
    def list_product(root):
        from Model.product_db import DataBaseProduct
        from View.adm_screen import admin_roles
        from View.adm_product_screen import list_product

        result_search = DataBaseProduct.select_product_all()
        if result_search:
            root.destroy()
            list_product(result_search)
        else:
            messagebox.showinfo('INFORMAÇÃO', 'Nenhum produto cadastrado com esse ID.')
            root.destroy()
            admin_roles()