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

def remove_product_screen():
    from View.adm_screen import admin_roles
    from Controller.adm_product import AdminProduct

    root = tk.Tk()
    root.title('Super Kernel - Remover Produtos')
    root.geometry('1300x800')
    root.resizable(False, False)
    root.config(bg= 'White')
    root.iconphoto(False, tk.PhotoImage(file = 'View/imgs/logo.png'))

    frame_barr = tk.Frame(root, width= 1300, height= 100, bg= '#d52b1e')
    frame_barr.pack()
    frame_barr.pack_propagate(False)

    location_img = tk.PhotoImage(file='./View/imgs/sem_bg.png')
    location_img = location_img.subsample(4, 4)
    logo_label = tk.Label(frame_barr, width= 200, height= 200, image=location_img, bg= '#d52b1e')
    logo_label.place(x= 550, y= -40)

    box_frame = tk.Frame(root, width= 1100, height= 600, bg= '#d52b1e')
    box_frame.place(x= 102, y= 150)
    box_frame.pack_propagate(False)

    remove_label = tk.Label(box_frame, width= 15, height= 1, text='Remover Produto', font = ('Berlin Sans FB', 20, 'bold'), fg = 'white', bg= '#d52b1e')
    remove_label.place(x= 430, y= 30)

    id_product_label = tk.Label(box_frame, width= 15, height= 1, text='Id do Produto:', font = ('Berlin Sans FB', 14), fg = 'white', bg= '#d52b1e')
    id_product_label.place(x= 220, y= 150)

    id_product_entry = tk.Entry(box_frame, width= 50, font= ('Berlin Sans FB', 14), bg = '#e3e3e3', fg = '#9e9e9e')
    id_product_entry.place(x= 360, y= 150)

    name_product_label = tk.Label(box_frame, width= 15, height= 1, text='Nome do Produto:', font = ('Berlin Sans FB', 14), fg = 'white', bg= '#d52b1e', anchor= 'w')
    name_product_label.place(x= 200, y= 250)

    name_product_entry = tk.Entry(box_frame, width= 50, font= ('Berlin Sans FB', 14), bg = '#e3e3e3', fg = '#9e9e9e')
    name_product_entry.place(x= 360, y= 250)

    button_remove = tk.Button(box_frame, width = 20, height = 2, text='Remover', font = ('Berlin Sans FB', 14), fg = 'White', bg= '#d52b1e', relief='ridge',
                             activeforeground = '#d52b1e', command= lambda: (AdminProduct.remove_product(id= id_product_entry.get(), name= name_product_entry.get(), root= root),
                                                                                                         id_product_entry.delete(0, tk.END),
                                                                                                         name_product_entry.delete(0, tk.END))) 
    button_remove.place(x= 300, y= 400)

    button_quit = tk.Button(box_frame, width = 20, height = 2, text='Sair', font = ('Berlin Sans FB', 14), fg = 'White', bg= '#d52b1e', relief='ridge',
                             activeforeground = '#d52b1e', command= lambda: (root.destroy(), admin_roles()))
    button_quit.place(x= 600, y= 400)

    root.mainloop()

def edit_product_screen():
    from View.adm_screen import admin_roles
    from Controller.adm_product import AdminProduct


    root = tk.Tk()
    root.title('Super Kernel - Editar Produtos')
    root.geometry('1300x800')
    root.resizable(False, False)
    root.config(bg= 'White')
    root.iconphoto(False, tk.PhotoImage(file = 'View/imgs/logo.png'))

    frame_barr = tk.Frame(root, width= 1300, height= 100, bg= '#d52b1e')
    frame_barr.pack()
    frame_barr.pack_propagate(False)

    location_img = tk.PhotoImage(file='./View/imgs/sem_bg.png')
    location_img = location_img.subsample(4, 4)
    logo_label = tk.Label(frame_barr, width= 200, height= 200, image=location_img, bg= '#d52b1e')
    logo_label.place(x= 550, y= -40)

    box_frame = tk.Frame(root, width= 1100, height= 600, bg= '#d52b1e')
    box_frame.place(x= 102, y= 150)
    box_frame.pack_propagate(False)

    edit_title_label = tk.Label(box_frame, width= 15, height= 1, text='Editar Produto', font = ('Berlin Sans FB', 20, 'bold'), fg = 'white', bg= '#d52b1e')
    edit_title_label.place(x= 430, y= 30)

    id_product_label = tk.Label(box_frame, width= 15, height= 1, text='ID do Produto:', font = ('Berlin Sans FB', 14), fg = 'white', bg= '#d52b1e', anchor= 'w') 
    id_product_label.place(x=150, y=100)

    id_product_entry = tk.Entry(box_frame, width= 50, font= ('Berlin Sans FB', 14), bg = '#e3e3e3', fg = '#9e9e9e')  
    id_product_entry.place(x= 310, y= 100) 

    name_product_label = tk.Label(box_frame, width= 15, height= 1, text='Nome do Produto:', font = ('Berlin Sans FB', 14), fg = 'white', bg= '#d52b1e', anchor= 'w') 
    name_product_label.place(x=150, y=150)

    name_product_entry = tk.Entry(box_frame, width= 50, font= ('Berlin Sans FB', 14), bg = '#e3e3e3', fg = '#9e9e9e')  
    name_product_entry.place(x= 310, y= 150) 

    qnt_stock_label = tk.Label(box_frame, width= 15, height= 1, text='Estoque:', font = ('Berlin Sans FB', 14), fg = 'white', bg= '#d52b1e' ) 
    qnt_stock_label.place(x=190, y=200)

    qnt_stock_entry = tk.Entry(box_frame, width= 50, font= ('Berlin Sans FB', 14), bg = '#e3e3e3', fg = '#9e9e9e')  
    qnt_stock_entry.place(x= 310, y= 200) 

    price_product_label = tk.Label(box_frame, width= 15, height= 1, text='Preço:', font = ('Berlin Sans FB', 14), fg = 'white', bg= '#d52b1e') 
    price_product_label.place(x=200, y=250)

    price_product_entry = tk.Entry(box_frame, width= 50, font= ('Berlin Sans FB', 14), bg = '#e3e3e3', fg = '#9e9e9e')  
    price_product_entry.place(x= 310, y= 250) 

    description_product_label = tk.Label(box_frame, width= 15, height= 1, text='Descrição:', font = ('Berlin Sans FB', 14), fg = 'white', bg= '#d52b1e') 
    description_product_label.place(x=185, y=300)

    description_product_entry = tk.Entry(box_frame, width= 50, font= ('Berlin Sans FB', 14), bg = '#e3e3e3', fg = '#9e9e9e')  
    description_product_entry.place(x= 310, y= 300)  

    button_remove = tk.Button(box_frame, width = 20, height = 2, text='Editar', font = ('Berlin Sans FB', 14), fg = 'White', bg= '#d52b1e', relief='ridge',
                             activeforeground = '#d52b1e', command= lambda: (AdminProduct.edit_product(id= id_product_entry.get(), name= name_product_entry.get(),
                                                                                                       stock= qnt_stock_entry.get(), price= price_product_entry.get(),
                                                                                                       description= description_product_entry.get(), root= root),
                                                                                                       id_product_entry.delete(0, tk.END), name_product_entry.delete(0, tk.END),
                                                                                                       qnt_stock_entry.delete(0, tk.END), price_product_entry.delete(0, tk.END),
                                                                                                       description_product_entry.delete(0, tk.END)))
    button_remove.place(x= 300, y= 500)

    button_quit = tk.Button(box_frame, width = 20, height = 2, text='Sair', font = ('Berlin Sans FB', 14), fg = 'White', bg= '#d52b1e', relief='ridge',
                             activeforeground = '#d52b1e', command= lambda: (root.destroy(), admin_roles()))
    button_quit.place(x= 600, y= 500)

    root.mainloop()

def list_product(result):
    from View.adm_screen import admin_roles


    root = tk.Tk()
    root.title('Super Kernel - Listar Produtos')
    root.geometry('1300x800')
    root.resizable(False, False)
    root.config(bg= 'White')
    root.iconphoto(False, tk.PhotoImage(file = 'View/imgs/logo.png'))

    frame_barr = tk.Frame(root, width= 1300, height= 100, bg= '#d52b1e')
    frame_barr.pack()
    frame_barr.pack_propagate(False)

    location_img = tk.PhotoImage(file='./View/imgs/sem_bg.png')
    location_img = location_img.subsample(4, 4)
    logo_label = tk.Label(frame_barr, width= 200, height= 200, image=location_img, bg= '#d52b1e')
    logo_label.place(x= 550, y= -40)

    box_frame = tk.Frame(root, width= 1300, height= 700, bg= 'white')
    box_frame.pack()
    box_frame.pack_propagate(False)

    tv = ttk.Treeview(box_frame, columns=('id', 'name', 'stock', 'price', 'category'), show= 'headings')
    tv.column('id', minwidth= 0, width= 50)
    tv.column('name', minwidth= 0, width= 250)
    tv.column('stock', minwidth= 0, width= 50)
    tv.column('price', minwidth= 0, width= 100)
    tv.column('category', minwidth= 0, width= 50)
    tv.heading('id', text= 'ID')
    tv.heading('name', text= 'NOME')
    tv.heading('stock', text= 'ESTOQUE')
    tv.heading('price', text= 'PREÇO')
    tv.heading('category', text= 'CATEGORIA')

    tv.tag_configure('header', background='#d52b1e', foreground='white')

    tv.tag_configure('odd', background='#f4f4f4')  
    tv.tag_configure('even', background='#ffffff')  

    scrollbar = tk.Scrollbar(box_frame, orient='vertical', command=tv.yview)
    tv.configure(yscrollcommand=scrollbar.set)

    tv.pack(side='left', fill='both', expand=True)
    scrollbar.pack(side='right', fill='y')

    for idx, (id_product, name_product, qnt_stock, price, category_id, description) in enumerate(result):
        tag = 'odd' if idx % 2 == 0 else 'even'
        
        item_id = tv.insert('', 'end', values=(id_product, name_product, qnt_stock, price, category_id))
        tv.item(item_id, tags=(tag,))

    button_quit = tk.Button(frame_barr, width = 10, height = 1, text='Sair', font = ('Berlin Sans FB', 14), fg = 'White', bg= '#d52b1e', relief='ridge',
                             activeforeground = '#d52b1e', command= lambda: (root.destroy(), admin_roles()))
    button_quit.place(x= 30, y= 30)

    root.mainloop()
