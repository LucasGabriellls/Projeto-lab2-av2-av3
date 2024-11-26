import tkinter as tk
import tkinter.ttk as ttk


from View.home import sign_in

def buy():
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
                             activeforeground = '#d52b1e', command= lambda: (root.destroy(), sign_in()))
    button_quit.place(x= 20, y= 30)

    button_confirm_buy = tk.Button(frame_barr, width = 10, height = 1, text='Carrinho', font = ('Berlin Sans FB', 14), fg = 'White', bg= '#d52b1e', relief='ridge',
                             activeforeground = '#d52b1e')
    button_confirm_buy.place(x= 1170, y= 30)
    
    search_label = tk.Label(root, width= 15, height= 1, text='Nome do Produto:', font = ('Berlin Sans FB', 14), fg = '#d52b1e', bg= 'white', anchor= 'w')
    search_label.place(x= 0, y= 100)

    search_entry = tk.Entry(root, width= 50, font= ('Berlin Sans FB', 14), bg = '#e3e3e3', fg = '#9e9e9e')
    search_entry.place(x= 160, y= 102)

    filter_label = tk.Label(root, width= 10, height= 1, text='Filtros:', font = ('Berlin Sans FB', 14), fg = '#d52b1e', bg= 'white', anchor= 'w')
    filter_label.place(x= 730, y= 102)

    search_filter_combox = ttk.Combobox(root, width= 50)
    search_filter_combox['values'] = 'Valor Crescente', 'Valor Decrescente', 'Ordem Alfabética', 'Relevantes'
    search_filter_combox.place(x= 800, y= 105)

    root.mainloop()    