import tkinter as tk


def record():
    from Controller.user import User

    
    root = tk.Tk()
    root.title('Super Kernel')
    root.geometry('1300x800')
    root.resizable(False, False)
    root.config(bg = 'white')
    root.iconphoto(False, tk.PhotoImage(file = 'View/imgs/logo.png'))

    frame_screen1 = tk.Frame(root, width = 500, height = 800, bg = '#d52b1e')
    frame_screen1.grid(row = 0)
    frame_screen1.pack_propagate(False)

    label_title_sign_in = tk.Label(frame_screen1, width = 30, height = 2, text='Bem-vindo de volta!', font = ('Berlin Sans FB', 30, 'bold'), fg = 'White', bg= '#d52b1e')
    label_title_sign_in.place(x = -115, y = 220)

    label_subtitle_sign_in = tk.Label(frame_screen1, width = 100, height = 2, text='Para manter-se conectado,\n por favor, faça login com suas informações pessoais.',
                            font = ('Berlin Sans FB', 14), fg = 'White', bg= '#d52b1e')
    label_subtitle_sign_in.place(x = -260, y = 300)

    button_sign_in = tk.Button(frame_screen1, width = 20, height = 2, text='ENTRAR', font = ('Berlin Sans FB', 11), relief ='ridge', bg ='#d52b1e', fg ='White', 
                                activeforeground = '#d52b1e', command = lambda: (root.destroy(), sign_in()))
    button_sign_in.place(x = 150, y = 400)

    label_title_register = tk.Label(root, width = 30, height = 2, text = 'Criar Conta', font = ('Berlin Sans FB', 30, 'bold'), bg ='white', fg = '#d52b1e')
    label_title_register.place(x = 550, y = 100)

    label_entry_title1 = tk.Label(root, width = 50, height = 2, text = 'Digite seu nome:', font = ('Berlin Sans FB', 11, 'bold'), bg = 'White', fg = '#d52b1e')
    label_entry_title1.place(x = 560, y = 300)

    entry_name = tk.Entry(root, width = 40, font = ('Berlin Sans FB', 11), bg = '#e3e3e3', fg = '#9e9e9e')
    entry_name.place(x = 725, y = 330)

    label_entry_title2 = tk.Label(root, width = 50, height = 2, text = 'Digite seu email:', font = ('Berlin Sans FB', 11, 'bold'), bg = 'White', fg = '#d52b1e')
    label_entry_title2.place(x = 560, y = 370)

    entry_email = tk.Entry(root, width = 40, font = ('Berlin Sans FB', 11), bg = '#e3e3e3', fg = '#9e9e9e')
    entry_email.place(x = 725, y = 400)

    label_entry_title3 = tk.Label(root, width = 50, height = 2, text = 'Digite sua senha:', font = ('Berlin Sans FB', 11, 'bold'), bg = 'White', fg = '#d52b1e')
    label_entry_title3.place(x = 560, y = 440)

    entry_password = tk.Entry(root, width = 40, font = ('Berlin Sans FB', 11), bg = '#e3e3e3', fg = '#9e9e9e', show = '*')
    entry_password.place(x = 725, y = 470)

    button_register = tk.Button(root, width = 20, height = 2, text = 'ENTRAR', font = ('Berlin Sans FB', 11), relief ='ridge', bg ='#d52b1e', fg ='White', 
                                activeforeground = '#d52b1e',  command=lambda: (User.validate_record(
                                User(name=entry_name.get(), email=entry_email.get(), password=entry_password.get()), root),
                                entry_name.delete(0, tk.END),
                                entry_email.delete(0, tk.END),
                                entry_password.delete(0, tk.END)))
    button_register.place(x = 820, y = 550)

    root.mainloop()


def sign_in():
    from Controller.user import User
    from Controller.user_buy import Buy


    root = tk.Tk()
    root.title('Super Kernel')
    root.geometry('1300x800')
    root.resizable(False, False)
    root.config(bg= 'White')
    root.iconphoto(False, tk.PhotoImage(file = 'View/imgs/logo.png'))

    frame_screen1 = tk.Frame(root, width= 500, height= 800, bg = '#d52b1e')
    frame_screen1.place(x= 800)
    frame_screen1.pack_propagate(False)

    label_title_frame = tk.Label(frame_screen1, width = 30, height = 2, text='Bem-vindo ao login!', font = ('Berlin Sans FB', 30, 'bold'), fg = 'White', bg= '#d52b1e')
    label_title_frame.place(x= -100, y= 250)

    button_record = tk.Button(frame_screen1, width= 20, height= 2, text='CADASTRAR', font = ('Berlin Sans FB', 11), relief ='ridge', bg ='#d52b1e', fg ='White', 
                                activeforeground = '#d52b1e', command= lambda: (root.destroy(), record()))
    button_record.place(x= 180, y= 450)

    label_subtitle_frame = tk.Label(frame_screen1, width = 100, height = 2, text='Ainda não possui uma conta?', font = ('Berlin Sans FB', 14), fg = 'White', bg= '#d52b1e')
    label_subtitle_frame.place(x= -240, y= 320)

    lable_title = tk.Label(root, width = 30, height = 2, text = 'Faça login para continuar!', font = ('Berlin Sans FB', 30, 'bold'), bg ='white', fg = '#d52b1e')
    lable_title.place(x= 40, y= 200)

    label_email = tk.Label(root, width = 50, height = 2, text = 'Digite seu email:', font = ('Berlin Sans FB', 11, 'bold'), bg = 'White', fg = '#d52b1e')
    label_email.place(x= 55, y= 320)

    entry_email = tk.Entry(root, width= 40, font= ('Berlin Sans FB', 11), bg= '#e3e3e3', fg= '#9e9e9e')
    entry_email.place(x= 220, y= 350)

    label_password = tk.Label(root, width= 50, height= 2, text= 'Digite sua senha:', font= ('Berlin Sans FB', 11, 'bold'), bg = 'White', fg = '#d52b1e')
    label_password.place(x= 55, y= 420)

    entry_password = tk.Entry(root, width= 40, font= ('Berlin Sans FB', 11), bg= '#e3e3e3', fg= '#9e9e9e', show= '*')
    entry_password.place(x= 220, y= 450)

    button_sign_in = tk.Button(root, width = 20, height = 2, text='ENTRAR', font = ('Berlin Sans FB', 11), relief ='ridge', bg ='#d52b1e', fg ='White', 
                                activeforeground = '#d52b1e', command= lambda: (
                                    User.validate_sign_in(User(email= entry_email.get(), password=entry_password.get()), root=root),
                                    entry_email.delete(0, tk.END),
                                    entry_password.delete(0, tk.END)))
    button_sign_in.place(x= 310, y= 550)

    root.mainloop()

def adm_sign_in(): 
    from Controller.adm import admin


    root = tk.Tk()
    root.title('Super Kernel')
    root.geometry('1300x800')
    root.resizable(False, False)
    root.config(bg= 'White')
    root.iconphoto(False, tk.PhotoImage(file = 'View/imgs/logo.png'))

    frame_bar = tk.Frame(root, width= 1300, height= 60, bg= '#d52b1e')
    frame_bar.pack_propagate(False)
    frame_bar.pack()

    title_label = tk.Label(frame_bar, width = 30, height = 2, text='Autenticação de dois fatores (2FA).', font = ('Berlin Sans FB', 20, 'bold'), fg = 'White', bg= '#d52b1e')
    title_label.pack()

    subtitle1_label = tk.Label(root,  width = 100, height = 1, text='1- Instale o aplicativo Google Authenticator no seu telefone.', font = ('Berlin Sans FB', 14), fg = '#d52b1e', bg= 'white')
    subtitle1_label.place(x= 150, y= 70)

    subtitle1_labe2 = tk.Label(root,  width = 100, height = 1, text='2- Escaneie o código QR abaixo com o seu aplicativo.', font = ('Berlin Sans FB', 14), fg = '#d52b1e', bg= 'white')
    subtitle1_labe2.place(x= 150, y= 120)

    location_img = tk.PhotoImage(file='./View/imgs/totp.png')
    location_img = location_img.subsample(2, 2)
    qr_code_label = tk.Label(root, width= 200, height= 200, image=location_img)
    qr_code_label.pack(pady= 100)
    
    subtitle1_labe3 = tk.Label(root,  width = 100, height = 1, text='3- Digite o código de 6 dígitos do Google Authenticator.', font = ('Berlin Sans FB', 14), fg = '#d52b1e', bg= 'white')
    subtitle1_labe3.place(x= 150, y= 400)

    code_entry = tk.Entry(root,  width= 40, font= ('Berlin Sans FB', 11), bg= '#e3e3e3', fg= '#9e9e9e')
    code_entry.place(x= 470, y= 450)

    button_sign_in = tk.Button(root, width = 20, height = 2, text='ENTRAR', font = ('Berlin Sans FB', 11), relief ='ridge', bg ='#d52b1e', fg ='White',  
                               activeforeground = '#d52b1e', command= lambda: (admin.validate_entry(admin(entry= code_entry.get()), root=root),
                                                                               code_entry.delete(0, tk.END)))
                                                                               
                                                                               
    button_sign_in.place(x= 470, y= 500)

    button_quit = tk.Button(root, width = 20, height = 2, text='SAIR', font = ('Berlin Sans FB', 11), relief ='ridge', bg ='#d52b1e', fg ='White',  
                            activeforeground = '#d52b1e', command= lambda: (root.destroy(), record()))
    button_quit.place(x= 664, y= 500)

    root.mainloop()
           