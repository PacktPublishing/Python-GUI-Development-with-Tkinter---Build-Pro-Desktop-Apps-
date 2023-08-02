import tkinter as tk

root = tk.Tk()
root.title("The spinbox application")
root.minsize(300,200)

tk.Spinbox(root,from_= 0, to=10, values=5).pack()


root.mainloop()