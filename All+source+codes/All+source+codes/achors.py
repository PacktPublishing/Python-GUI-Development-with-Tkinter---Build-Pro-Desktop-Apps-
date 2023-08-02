import tkinter as tk

root = tk.Tk()
root.title("widgets and anchors")
root.minsize(300,200)

frame = tk.Frame(root).pack()
tk.Label(root, text="North").pack(anchor= "s")



root.mainloop()