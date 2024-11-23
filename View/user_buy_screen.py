import tkinter as tk


def buy():
    root = tk.Tk()
    root.title('Super Kernel - Compra')
    root.geometry('1300x800')
    root.resizable(False, False)
    root.config(bg= 'White')
    root.iconphoto(False, tk.PhotoImage(file = 'View/imgs/logo.png'))

    frame_barr = tk.Frame(root, width= 1300, height= 50, bg= '#d52b1e')
    frame_barr.pack()
    
    root.mainloop()    