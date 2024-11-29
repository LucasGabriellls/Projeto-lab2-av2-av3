import tkinter as tk
import tkinter.ttk as ttk


from View.home import sign_in

def buy(product):
    from Controller.user_buy import Buy


    root = tk.Tk()
    root.title('Super Kernel - Compra')
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

    button_quit = tk.Button(frame_barr, width = 10, height = 1, text='SAIR', font = ('Berlin Sans FB', 14), fg = 'White', bg= '#d52b1e', relief='ridge',
                             activeforeground = '#d52b1e', command= lambda: (Buy.quit_buy(root)))
    button_quit.place(x= 20, y= 30)

    button_confirm_buy = tk.Button(frame_barr, width = 10, height = 1, text='Carrinho', font = ('Berlin Sans FB', 14), fg = 'White', bg= '#d52b1e', relief='ridge',
                             activeforeground = '#d52b1e', command= lambda: (Buy.cart_market(root)))
    button_confirm_buy.place(x= 1170, y= 30)
    
    search_label = tk.Label(root, width= 15, height= 1, text='Nome do Produto:', font = ('Berlin Sans FB', 14), fg = '#d52b1e', bg= 'white', anchor= 'w')
    search_label.place(x= 0, y= 100)

    search_entry = tk.Entry(root, width= 50, font= ('Berlin Sans FB', 14), bg = '#e3e3e3', fg = '#9e9e9e')
    search_entry.place(x= 160, y= 102)

    filter_label = tk.Label(root, width= 10, height= 1, text='Filtros:', font = ('Berlin Sans FB', 14), fg = '#d52b1e', bg= 'white', anchor= 'w')
    filter_label.place(x= 730, y= 102)

    search_filter_combox = ttk.Combobox(root, width= 50)
    search_filter_combox['values'] = 'Valor Crescente', 'Valor Decrescente', 'Ordem Alfabética'
    search_filter_combox.place(x= 800, y= 105)

    box_frame = tk.Frame(root, width= 1300, height= 600, bg= 'white')
    box_frame.place(x= 0, y= 130)
    box_frame.pack_propagate(False)

    tv = ttk.Treeview(box_frame, columns=('id_product', 'name', 'price'), show= 'headings')
    tv.column('id_product', minwidth= 0, width= 100)
    tv.column('name', minwidth= 0, width= 250)
    tv.column('price', minwidth= 0, width= 100)

    tv.heading('id_product', text= 'ID')
    tv.heading('name', text= 'NOME')
    tv.heading('price', text= 'PREÇO')

    tv.tag_configure('header', background='#d52b1e', foreground='white')

    tv.tag_configure('odd', background='#f4f4f4')  
    tv.tag_configure('even', background='#ffffff')  

    scrollbar = tk.Scrollbar(box_frame, orient='vertical', command=tv.yview)
    tv.configure(yscrollcommand=scrollbar.set)

    tv.pack(side='left', fill='both', expand=True)
    scrollbar.pack(side='right', fill='y')
    
    for idx, (id_product, name_product, qnt_stock, price, category_id, description) in enumerate(product):
        tag = 'odd' if idx % 2 == 0 else 'even'
        
        item_id = tv.insert('', 'end', values=(id_product, name_product, price))
        tv.item(item_id, tags=(tag,))

    button_filter = tk.Button(root, width= 15, height= 1, text= 'Habilitar Filtro', font = ('Berlin Sans FB', 14), fg = 'White', bg= '#d52b1e', relief='ridge',
                             activeforeground = '#d52b1e', command= lambda: (Buy.list_filter(root, key_word_combox= search_filter_combox.get(), 
                                                                                             key_word_entry= search_entry.get()),
                                                                                             search_entry.delete(0, tk.END)))
    button_filter.place(x= 20, y= 750)

    buy_label = tk.Label(root, width= 20, height= 2, text= 'Comprar [DIGITAR ID]:',font = ('Berlin Sans FB', 14), fg = '#d52b1e', bg= 'white')
    buy_label.place(x= 300, y= 740)

    buy_entry = tk.Entry(root, width= 30, font= ('Berlin Sans FB', 14), bg = '#e3e3e3', fg = '#9e9e9e')
    buy_entry.place(x= 500, y= 752)

    button_ok = tk.Button(root, width= 5, height= 1, text= 'OK', font = ('Berlin Sans FB', 14), fg = 'White', bg= '#d52b1e', relief='ridge',
                             activeforeground = '#d52b1e', command= lambda: (Buy.check_buy(id_product= buy_entry.get(), amount= qnt_entry.get()),
                                                                             buy_entry.delete(0, tk.END),
                                                                             qnt_entry.delete(0, tk.END)))
    button_ok.place(x= 1150, y= 748)

    qnt_label = tk.Label(root, width= 15, height= 2, text= 'Quantidade:',font = ('Berlin Sans FB', 14), fg = '#d52b1e', bg= 'white')
    qnt_label.place(x= 750, y= 740)

    qnt_entry = tk.Entry(root, width= 15, font= ('Berlin Sans FB', 14), bg = '#e3e3e3', fg = '#9e9e9e')
    qnt_entry.place(x= 890, y= 752)

    root.mainloop()    

def cart_screen(orders):
    root = tk.Tk()
    root.title('Super Kernel - Compra')
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

    box_frame = tk.Frame(root, width=1300, height=300, bg='white')
    box_frame.pack(fill='both', expand=True)  

    tv = ttk.Treeview(box_frame, columns=('name_product', 'amount'), show='headings')
    tv.column('name_product', minwidth=0, width=100)
    tv.column('amount', minwidth=0, width=250)

    tv.heading('name_product', text='NOME')
    tv.heading('amount', text='QUANTIDADE')

    tv.tag_configure('header', background='#d52b1e', foreground='white')
    tv.tag_configure('odd', background='#f4f4f4')  
    tv.tag_configure('even', background='#ffffff')

    scrollbar = tk.Scrollbar(box_frame, orient='vertical', command=tv.yview)
    tv.configure(yscrollcommand=scrollbar.set)

    tv.pack(side='left', fill='both', expand=True)
    scrollbar.pack(side='right', fill='y')
    
    for idx, (name_product, amount) in enumerate(orders):
        tag = 'odd' if idx % 2 == 0 else 'even'
        item_id = tv.insert('', 'end', values=(name_product, amount))
        tv.item(item_id, tags=(tag,))

        root.mainloop()
    
