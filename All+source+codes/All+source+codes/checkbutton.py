import tkinter as tk

root = tk.Tk()
root.title("The Checkbutton Widget")
root.minsize(300,200)

tk.Label(root,text="Select Your Best Fruit").pack()

tk.Checkbutton(root,text="Mango").pack()
tk.Checkbutton(root,text="Banana").pack()
tk.Checkbutton(root,text="Apple").pack()
tk.Checkbutton(root,text="Grape").pack()
tk.Checkbutton(root,text="Grapefruit").pack()
tk.Checkbutton(root,text="Metabrains", state="disabled").pack()


root.mainloop()