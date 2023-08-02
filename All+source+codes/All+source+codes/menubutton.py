import tkinter as tk

root = tk.Tk()
root.title("Menu with Menubutton")
root.minsize(300,200)

menubutton = tk.Menubutton(root, text="select optios")

menu = tk.Menu(menubutton, tearoff= False)
menubutton["menu"] = menu
menu.add_command(label="Option 1")
menu.add_command(label="Option 2")
menu.add_command(label="Option 3")
menu.add_command(label="Option 4")

menubutton.pack()

root.mainloop()