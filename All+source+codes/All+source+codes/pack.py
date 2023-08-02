import tkinter as tk

root = tk.Tk()
root.title("Ther Packer")
root.minsize(300,200)

tk.Button(root, text="default Position").pack()
tk.Button(root, text="default Position attibutes").pack(side="right", anchor="center", fill="x", expand=1)


root.mainloop()