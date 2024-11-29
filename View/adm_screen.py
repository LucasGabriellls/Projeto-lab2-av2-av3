import tkinter as tk
import tkinter.ttk as ttk

from View.home import sign_in


def admin_roles():
    from View.adm_product_screen import add_product_screen, list_product
    from Controller.adm import admin
    from Controller.adm_product import AdminProduct
    from Controller.adm_user import AdminUser


    root = tk.Tk()
    root.title('Super kernel - Página de Administrador')
    root.geometry('1300x800')
    root.resizable(False, False)
    root.config(bg= 'White')
    root.iconphoto(False, tk.PhotoImage(file = 'View/imgs/logo.png'))

    frame_barr = tk.Frame(root, width= 300, height= 800, bg= '#d52b1e')
    frame_barr.grid(row= 0, column= 0)
    frame_barr.pack_propagate(False)

    location_img = tk.PhotoImage(file='./View/imgs/sem_bg.png')
    location_img = location_img.subsample(4, 4)
    logo_label = tk.Label(frame_barr, width= 200, height= 200, image=location_img, bg= '#d52b1e')
    logo_label.place(x= 50, y= -30)

    func_product_label = tk.Label(frame_barr, width = 30, height = 1, text='Produtos:', font = ('Berlin Sans FB', 14), fg = 'White', bg= '#f44141', anchor='w')
    func_product_label.place(x= 1, y= 110)

    func1_product_button = tk.Button(frame_barr, width = 30, height = 1, text='Adicionar Produtos', font = ('Berlin Sans FB', 14), fg = 'White', bg= '#d52b1e', relief='ridge',
                             activeforeground = '#d52b1e', command= lambda: (root.destroy(), add_product_screen()))
    func1_product_button.place(x= -4, y= 140)

    func2_product_button = tk.Button(frame_barr, width = 30, height = 1, text='Remover Produto', font = ('Berlin Sans FB', 14), fg = 'White', bg= '#d52b1e', relief='ridge',
                             activeforeground = '#d52b1e', command= lambda: (admin.info_remove_product(root)))
    func2_product_button.place(x= -4, y= 180)

    func3_product_button = tk.Button(frame_barr, width = 30, height = 1, text='Listar Produto', font = ('Berlin Sans FB', 14), fg = 'White', bg= '#d52b1e', relief='ridge',
                             activeforeground = '#d52b1e', command= lambda: (AdminProduct.list_product(root)))
    func3_product_button.place(x= -4, y= 220)

    func4_product_button = tk.Button(frame_barr, width = 30, height = 1, text='Editar Produto', font = ('Berlin Sans FB', 14), fg = 'White', bg= '#d52b1e', relief='ridge',
                             activeforeground = '#d52b1e', command= lambda: (admin.info_edit_product(root)))
    func4_product_button.place(x= -4, y= 260)

    func_user_label = tk.Label(frame_barr, width = 30, height = 1, text='Usuário:', font = ('Berlin Sans FB', 14), fg = 'White', bg= '#f44141', anchor='w')
    func_user_label.place(x= 1, y= 300)

    func1_user_button = tk.Button(frame_barr, width = 30, height = 1, text='Remover Usuário', font = ('Berlin Sans FB', 14), fg = 'White', bg= '#d52b1e', relief='ridge',
                             activeforeground = '#d52b1e', command= lambda: (admin.info_remove_user(root)))
    func1_user_button.place(x= -4, y= 330)

    func2_user_button = tk.Button(frame_barr, width = 30, height = 1, text='Listar Usuários', font = ('Berlin Sans FB', 14), fg = 'White', bg= '#d52b1e', relief='ridge',
                             activeforeground = '#d52b1e', command= lambda: (AdminUser.list_user(root= root)))
    func2_user_button.place(x= -4, y= 370)

    func3_user_button = tk.Button(frame_barr, width = 30, height = 1, text='Editar Usuário', font = ('Berlin Sans FB', 14), fg = 'White', bg= '#d52b1e', relief='ridge',
                             activeforeground = '#d52b1e', command= lambda: (admin.info_edit_user(root)))
    func3_user_button.place(x= -4, y= 410)

    func_buy_label = tk.Label(frame_barr, width = 30, height = 1, text='Compra:', font = ('Berlin Sans FB', 14), fg = 'White', bg= '#f44141', anchor='w')
    func_buy_label.place(x= 1, y= 450)

    func1_buy_button = tk.Button(frame_barr, width = 30, height = 1, text='Compras por Cliente', font = ('Berlin Sans FB', 14), fg = 'White', bg= '#d52b1e', relief='ridge',
                             activeforeground = '#d52b1e')
    func1_buy_button.place(x= -4, y= 480)

    func2_buy_button = tk.Button(frame_barr, width = 30, height = 1, text='Produtos mais Vendidos', font = ('Berlin Sans FB', 14), fg = 'White', bg= '#d52b1e', relief='ridge',
                             activeforeground = '#d52b1e')
    func2_buy_button.place(x= -4, y= 520)

    func3_buy_button = tk.Button(frame_barr, width = 30, height = 1, text='Informações Gerais', font = ('Berlin Sans FB', 14), fg = 'White', bg= '#d52b1e', relief='ridge',
                             activeforeground = '#d52b1e')
    func3_buy_button.place(x= -4, y= 560)

    quit_button = tk.Button(frame_barr, width = 20, height = 2, text='Sair', font = ('Berlin Sans FB', 14), fg = 'White', bg= '#d52b1e', relief='ridge',
                             activeforeground = '#d52b1e', command= lambda: (root.destroy(), sign_in()))
    quit_button.place(x= 45, y= 650)

    title_label = tk.Label(root, width= 30, height= 2, text='Área do Administrador', font = ('Berlin Sans FB', 20, 'bold'), fg = '#d52b1e', bg= 'White')
    title_label.place(x= 570, y= 10)

    logo_location_img = tk.PhotoImage(file='./View/imgs/logo.png')
    logo_img_label = tk.Label(root, width= 500, height= 500, image= logo_location_img, bg= 'white')
    logo_img_label.place(x= 560, y= 150)

    root.mainloop()