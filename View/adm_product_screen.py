import tkinter as tk

def add_product_screen():
    root = tk.Tk()
    root.title('Super Kernel - Adicionar Produtos')
    root.geometry('1300x800')
    root.resizable(False, False)
    root.config(bg= 'White')
    root.iconphoto(False, tk.PhotoImage(file = 'View/imgs/logo.png'))

    box_frame = tk.Frame(root, width= 1000, height= 600, bg= '#d52b1e')
    box_frame.place(x= 150, y= 111)
    box_frame.pack_propagate(False)

    title_label = tk.Label(root, width= 20, height= 2, text= 'Adicionar Produtos', font= ('Berlin Sans FB', 30, 'bold'), fg= '#d52b1e', bg= 'white')
    title_label.pack(pady= 5)

    root.mainloop()