import tkinter as tk
from tkinter import ttk


def remove_user_screen():
    from View.adm_screen import admin_roles
    from Controller.adm_user import AdminUser


    root = tk.Tk()
    root.title('Super Kernel - Remover Usuário')
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

    remove_label = tk.Label(box_frame, width= 15, height= 1, text='Remover Usuário', font = ('Berlin Sans FB', 20, 'bold'), fg = 'white', bg= '#d52b1e')
    remove_label.place(x= 430, y= 30)

    id_user_label = tk.Label(box_frame, width= 15, height= 1, text='Id do Usuário:', font = ('Berlin Sans FB', 14), fg = 'white', bg= '#d52b1e')
    id_user_label.place(x= 220, y= 150)

    id_user_entry = tk.Entry(box_frame, width= 50, font= ('Berlin Sans FB', 14), bg = '#e3e3e3', fg = '#9e9e9e')
    id_user_entry.place(x= 360, y= 150)

    name_user_label = tk.Label(box_frame, width= 15, height= 1, text='Nome do Usuário:', font = ('Berlin Sans FB', 14), fg = 'white', bg= '#d52b1e', anchor= 'w')
    name_user_label.place(x= 200, y= 250)

    name_user_entry = tk.Entry(box_frame, width= 50, font= ('Berlin Sans FB', 14), bg = '#e3e3e3', fg = '#9e9e9e')
    name_user_entry.place(x= 360, y= 250)

    button_remove = tk.Button(box_frame, width = 20, height = 2, text='Remover', font = ('Berlin Sans FB', 14), fg = 'White', bg= '#d52b1e', relief='ridge',
                             activeforeground = '#d52b1e', command= lambda: (AdminUser.remove_user(id= id_user_entry.get(), name= name_user_entry.get()),
                                                                             id_user_entry.delete(0, tk.END),
                                                                             name_user_entry.delete(0, tk.END)))
    button_remove.place(x= 300, y= 400)

    button_quit = tk.Button(box_frame, width = 20, height = 2, text='Sair', font = ('Berlin Sans FB', 14), fg = 'White', bg= '#d52b1e', relief='ridge',
                             activeforeground = '#d52b1e', command= lambda: (root.destroy(), admin_roles()))
    button_quit.place(x= 600, y= 400)

    root.mainloop()

def edit_user_screen():
    from View.adm_screen import admin_roles


    root = tk.Tk()
    root.title('Super Kernel - Editar Usuário')
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

    edit_title_label = tk.Label(box_frame, width= 15, height= 1, text='Editar Usuário', font = ('Berlin Sans FB', 20, 'bold'), fg = 'white', bg= '#d52b1e')
    edit_title_label.place(x= 430, y= 30)

    id_user_label = tk.Label(box_frame, width= 15, height= 1, text='ID do Usuário:', font = ('Berlin Sans FB', 14), fg = 'white', bg= '#d52b1e', anchor= 'w') 
    id_user_label.place(x=150, y=100)

    id_user_entry = tk.Entry(box_frame, width= 50, font= ('Berlin Sans FB', 14), bg = '#e3e3e3', fg = '#9e9e9e')  
    id_user_entry.place(x= 310, y= 100) 

    name_user_label = tk.Label(box_frame, width= 15, height= 1, text='Nome do Usuário:', font = ('Berlin Sans FB', 14), fg = 'white', bg= '#d52b1e', anchor= 'w') 
    name_user_label.place(x=150, y=150)

    name_user_entry = tk.Entry(box_frame, width= 50, font= ('Berlin Sans FB', 14), bg = '#e3e3e3', fg = '#9e9e9e')  
    name_user_entry.place(x= 310, y= 150) 

    address_user_label = tk.Label(box_frame, width= 15, height= 1, text='Endereço:', font = ('Berlin Sans FB', 14), fg = 'white', bg= '#d52b1e' ) 
    address_user_label.place(x=190, y=200)

    address_user_entry = tk.Entry(box_frame, width= 50, font= ('Berlin Sans FB', 14), bg = '#e3e3e3', fg = '#9e9e9e')  
    address_user_entry.place(x= 310, y= 200) 

    nation_user_label = tk.Label(box_frame, width= 15, height= 1, text='País:', font = ('Berlin Sans FB', 14), fg = 'white', bg= '#d52b1e') 
    nation_user_label.place(x=200, y=250)

    nation_user_entry = tk.Entry(box_frame, width= 50, font= ('Berlin Sans FB', 14), bg = '#e3e3e3', fg = '#9e9e9e')  
    nation_user_entry.place(x= 310, y= 250) 

    email_user_label = tk.Label(box_frame, width= 15, height= 1, text='Email:', font = ('Berlin Sans FB', 14), fg = 'white', bg= '#d52b1e') 
    email_user_label.place(x=185, y=300)

    email_user_entry = tk.Entry(box_frame, width= 50, font= ('Berlin Sans FB', 14), bg = '#e3e3e3', fg = '#9e9e9e')  
    email_user_entry.place(x= 310, y= 300)  

    phone_user_label = tk.Label(box_frame, width= 15, height= 1, text='Telefone:', font = ('Berlin Sans FB', 14), fg = 'white', bg= '#d52b1e') 
    phone_user_label.place(x=185, y=350)

    phone_user_entry = tk.Entry(box_frame, width= 50, font= ('Berlin Sans FB', 14), bg = '#e3e3e3', fg = '#9e9e9e')  
    phone_user_entry.place(x= 310, y= 350) 

    button_remove = tk.Button(box_frame, width = 20, height = 2, text='Editar', font = ('Berlin Sans FB', 14), fg = 'White', bg= '#d52b1e', relief='ridge',
                             activeforeground = '#d52b1e')
    button_remove.place(x= 300, y= 500)

    button_quit = tk.Button(box_frame, width = 20, height = 2, text='Sair', font = ('Berlin Sans FB', 14), fg = 'White', bg= '#d52b1e', relief='ridge',
                             activeforeground = '#d52b1e', command= lambda: (root.destroy(), admin_roles()))
    button_quit.place(x= 600, y= 500)

    root.mainloop()

def list_user(user):
    from View.adm_screen import admin_roles


    root = tk.Tk()
    root.title('Super Kernel - Listar Usuário')
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

    tv = ttk.Treeview(box_frame, columns=('id', 'name', 'email_user'), show= 'headings')
    tv.column('id', minwidth= 0, width= 50)
    tv.column('name', minwidth= 0, width= 250)
    tv.column('email_user', minwidth= 0, width= 50)

    tv.heading('id', text= 'ID')
    tv.heading('name', text= 'NOME')
    tv.heading('email_user', text= 'EMAIL')

    tv.tag_configure('header', background='#d52b1e', foreground='white')

    tv.tag_configure('odd', background='#f4f4f4')  
    tv.tag_configure('even', background='#ffffff')  

    scrollbar = tk.Scrollbar(box_frame, orient='vertical', command=tv.yview)
    tv.configure(yscrollcommand=scrollbar.set)

    tv.pack(side='left', fill='both', expand=True)
    scrollbar.pack(side='right', fill='y')

    for idx, (id_product, name_user, email_user) in enumerate(user):
        tag = 'odd' if idx % 2 == 0 else 'even'
        
        item_id = tv.insert('', 'end', values=(id_product, name_user, email_user))
        tv.item(item_id, tags=(tag,))

    button_quit = tk.Button(frame_barr, width = 10, height = 1, text='Sair', font = ('Berlin Sans FB', 14), fg = 'White', bg= '#d52b1e', relief='ridge',
                             activeforeground = '#d52b1e', command= lambda: (root.destroy(), admin_roles()))
    button_quit.place(x= 30, y= 30)

    root.mainloop()
