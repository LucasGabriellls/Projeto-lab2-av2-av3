import tkinter as tk
import tkinter.ttk as ttk

def admin_roles():
    root = tk.Tk()
    root.title('Super kernel')
    root.geometry('1300x800')
    root.resizable(False, False)
    root.config(bg= 'White')
    root.iconphoto(False, tk.PhotoImage(file = 'View/imgs/logo.png'))

    location_img = tk.PhotoImage(file='./View/imgs/logo.png')
    location_img = location_img.subsample(6, 6)
    logo_lable = tk.Label(root, width=50, height=50, image=location_img)
    logo_lable.pack(pady=2)

    frame_bar = tk.Frame(root, width= 1300, height= 50, bg= '#d52b1e')
    frame_bar.place(x= 0, y= 60)
    frame_bar.pack_propagate(False)

    frame_box = tk.Frame(root, width=1100, height= 600, bg= '#d52b1e')
    frame_box.place(x=100, y= 155)
    frame_box.pack_propagate(False)

    root.mainloop()