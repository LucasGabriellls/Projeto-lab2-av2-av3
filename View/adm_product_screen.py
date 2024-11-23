import tkinter as tk
import tkinter.ttk as ttk


def add_product_screen():
    from Controller.adm import admin
    from View.adm_screen import admin_roles


    root = tk.Tk()
    root.title('Super Kernel - Adicionar Produtos')
    root.geometry('1300x800')
    root.resizable(False, False)
    root.config(bg= 'White')
    root.iconphoto(False, tk.PhotoImage(file = 'View/imgs/logo.png'))

    title_label = tk.Label(root, width= 20, height= 2, text= 'Adicionar Produtos', font= ('Berlin Sans FB', 30, 'bold'), fg= '#d52b1e', bg= 'white')
    title_label.pack(pady= 5)

    box_frame = tk.Frame(root, width= 1000, height= 600, bg= '#d52b1e')
    box_frame.place(x= 150, y= 111)
    box_frame.pack_propagate(False)

    name_label = tk.Label(box_frame, width= 50, height= 2, text = '*Nome do Produto:', font = ('Berlin Sans FB', 11, 'bold'), bg = '#d52b1e', fg = 'white')
    name_label.place(x= -112, y= 20)

    name_entry = tk.Entry(box_frame, width = 100,  font = ('Berlin Sans FB', 11), bg = '#e3e3e3', fg = '#9e9e9e')
    name_entry.place(x= 50, y= 50)

    qnt_stock_label = tk.Label(box_frame, width= 50, height= 2, text= 'Quantidade para Estoque:', font = ('Berlin Sans FB', 11, 'bold'), bg = '#d52b1e', fg = 'white')
    qnt_stock_label.place(x= -85, y= 80)

    qnt_stock_entry = tk.Entry(box_frame, width= 50, font = ('Berlin Sans FB', 11), bg = '#e3e3e3', fg = '#9e9e9e')
    qnt_stock_entry.place(x= 50, y= 110)

    price_label = tk.Label(box_frame, width= 50, height= 2, text= '*Preço:', font = ('Berlin Sans FB', 11, 'bold'), bg = '#d52b1e', fg = 'white')
    price_label.place(x= -152, y= 140)

    price_entry = tk.Entry(box_frame, width= 50, font = ('Berlin Sans FB', 11), bg = '#e3e3e3', fg = '#9e9e9e')
    price_entry.place(x= 50, y= 170)

    name_category = tk.Label(box_frame, width= 50, height= 2, text= '*Nome da Categoria:', font = ('Berlin Sans FB', 11, 'bold'), bg = '#d52b1e', fg = 'white')
    name_category.place(x= 400, y= 200)

    categories = admin.categories()
    combobox = ttk.Combobox(box_frame, width= 30)
    combobox['values'] = categories
    combobox.place(x= 555, y= 230)

    new_category = tk.Label(box_frame, width= 50, height= 2,  text= 'Nova Categoria:', font = ('Berlin Sans FB', 11, 'bold'), bg = '#d52b1e', fg = 'white')
    new_category.place(x= -120, y= 202)

    name_new_category = tk.Entry(box_frame, width= 50, font = ('Berlin Sans FB', 11), bg = '#e3e3e3', fg = '#9e9e9e')
    name_new_category.place(x= 50, y= 232)

    description_label = tk.Label(box_frame, width= 50, height= 2,  text= 'Descrição:', font = ('Berlin Sans FB', 11, 'bold'), bg = '#d52b1e', fg = 'white')
    description_label.place(x= -143, y= 260)

    description_entry = tk.Entry(box_frame, width= 100, font = ('Berlin Sans FB', 11), bg = '#e3e3e3', fg = '#9e9e9e')
    description_entry.place(x= 50, y= 290)

    button_confirm = tk.Button(box_frame, width = 20, height = 2, text = 'Confirmar', font = ('Berlin Sans FB', 11), relief ='ridge', bg ='#d52b1e', fg ='White', 
                                activeforeground = '#d52b1e', command= lambda: (admin.add_product(name_product= name_entry.get(), qnt_stock= qnt_stock_entry.get(),
                                                                                price= price_entry.get(), category= combobox.get(), new_category= name_new_category.get(),
                                                                                description= description_entry.get(), root= root),
                                                                                name_entry.delete(0, tk.END),
                                                                                qnt_stock_entry.delete(0, tk.END),
                                                                                price_entry.delete(0, tk.END),
                                                                                name_new_category.delete(0, tk.END),
                                                                                description_entry.delete(0, tk.END)))
    button_confirm.place(x= 300, y= 420)

    button_quit = tk.Button(box_frame, width = 20, height = 2, text = 'Sair', font = ('Berlin Sans FB', 11), relief ='ridge', bg ='#d52b1e', fg ='White', 
                                activeforeground = '#d52b1e', command= lambda: (root.destroy(), admin_roles()))
    button_quit.place(x= 500, y= 420)

    root.mainloop()