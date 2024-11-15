import tkinter as tk
import tkinter.ttk as ttk

from View.home import sign_in


def admin_roles():

    root = tk.Tk()
    root.title('Super kernel - Página de Administrador')
    root.geometry('1300x800')
    root.resizable(False, False)
    root.config(bg= 'White')
    root.iconphoto(False, tk.PhotoImage(file = 'View/imgs/logo.png'))

    frame_bar = tk.Frame(root, width= 300, height= 800, bg= '#d52b1e')
    frame_bar.grid(row= 0, column= 0)
    frame_bar.pack_propagate(False)

    title_label = tk.Label(frame_bar,  width = 30, height = 2, text='MENU', font = ('Berlin Sans FB', 20, 'bold'), fg = 'White', bg= '#d52b1e')
    title_label.pack(pady= 5)

    func_product_label = tk.Label(frame_bar, width = 30, height = 1, text='Produtos:', font = ('Berlin Sans FB', 14), fg = 'White', bg= '#f44141', anchor='w')
    func_product_label.place(x= 1, y= 110)

    func1_product_button = tk.Button(frame_bar, width = 30, height = 1, text='Adicionar Produtos', font = ('Berlin Sans FB', 14), fg = 'White', bg= '#d52b1e', relief='ridge',
                             activeforeground = '#d52b1e')
    func1_product_button.place(x= -4, y= 140)

    func2_product_button = tk.Button(frame_bar, width = 30, height = 1, text='Remover Produto', font = ('Berlin Sans FB', 14), fg = 'White', bg= '#d52b1e', relief='ridge',
                             activeforeground = '#d52b1e')
    func2_product_button.place(x= -4, y= 180)

    func3_product_button = tk.Button(frame_bar, width = 30, height = 1, text='Listar Produto', font = ('Berlin Sans FB', 14), fg = 'White', bg= '#d52b1e', relief='ridge',
                             activeforeground = '#d52b1e')
    func3_product_button.place(x= -4, y= 220)

    func4_product_button = tk.Button(frame_bar, width = 30, height = 1, text='Editar Produto', font = ('Berlin Sans FB', 14), fg = 'White', bg= '#d52b1e', relief='ridge',
                             activeforeground = '#d52b1e')
    func4_product_button.place(x= -4, y= 260)

    func_user_label = tk.Label(frame_bar, width = 30, height = 1, text='Usuário:', font = ('Berlin Sans FB', 14), fg = 'White', bg= '#f44141', anchor='w')
    func_user_label.place(x= 1, y= 300)

    func1_user_button = tk.Button(frame_bar, width = 30, height = 1, text='Remover Usuário', font = ('Berlin Sans FB', 14), fg = 'White', bg= '#d52b1e', relief='ridge',
                             activeforeground = '#d52b1e')
    func1_user_button.place(x= -4, y= 330)

    func2_user_button = tk.Button(frame_bar, width = 30, height = 1, text='Listar Usuários', font = ('Berlin Sans FB', 14), fg = 'White', bg= '#d52b1e', relief='ridge',
                             activeforeground = '#d52b1e')
    func2_user_button.place(x= -4, y= 370)

    func3_user_button = tk.Button(frame_bar, width = 30, height = 1, text='Editar Usuário', font = ('Berlin Sans FB', 14), fg = 'White', bg= '#d52b1e', relief='ridge',
                             activeforeground = '#d52b1e')
    func3_user_button.place(x= -4, y= 410)

    func_buy_label = tk.Label(frame_bar, width = 30, height = 1, text='Compra:', font = ('Berlin Sans FB', 14), fg = 'White', bg= '#f44141', anchor='w')
    func_buy_label.place(x= 1, y= 450)

    func1_buy_button = tk.Button(frame_bar, width = 30, height = 1, text='Compras por Cliente', font = ('Berlin Sans FB', 14), fg = 'White', bg= '#d52b1e', relief='ridge',
                             activeforeground = '#d52b1e')
    func1_buy_button.place(x= -4, y= 480)

    func2_buy_button = tk.Button(frame_bar, width = 30, height = 1, text='Produtos mais Vendidos', font = ('Berlin Sans FB', 14), fg = 'White', bg= '#d52b1e', relief='ridge',
                             activeforeground = '#d52b1e')
    func2_buy_button.place(x= -4, y= 520)

    func3_buy_button = tk.Button(frame_bar, width = 30, height = 1, text='Informações Gerais', font = ('Berlin Sans FB', 14), fg = 'White', bg= '#d52b1e', relief='ridge',
                             activeforeground = '#d52b1e')
    func3_buy_button.place(x= -4, y= 560)

    quit_button = tk.Button(frame_bar, width = 20, height = 2, text='Sair', font = ('Berlin Sans FB', 14), fg = 'White', bg= '#d52b1e', relief='ridge',
                             activeforeground = '#d52b1e', command= lambda: (root.destroy(), sign_in()))
    quit_button.place(x= 45, y= 650)


    info_frame = tk.Frame(root, width= 800, height= 600, bg= '#d52b1e')
    info_frame.place(x= 400, y=80)
    info_frame.pack_propagate(False)

    info_bar_frame = tk.Frame(info_frame, width= 800, height= 30, bg= '#f44141')
    info_bar_frame.place

    root.mainloop()

def add_product():
    root = tk.Tk()
    root.title('Super Kernel - Adicionar Produtos')
    root.geometry('1300x800')
    root.resizable(False, False)
    root.config(bg= 'White')
    root.iconphoto(False, tk.PhotoImage(file = 'View/imgs/logo.png'))

    
    root.mainloop()