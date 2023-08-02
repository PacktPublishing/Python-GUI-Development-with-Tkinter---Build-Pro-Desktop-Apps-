import tkinter as tk

root = tk.Tk()
root.title("placing widget")
root.minsize(300,200)

btn = tk.Button(root, text="mY PLACE")

btn.place(x=20, y=20, height=50, width=25)

root.mainloop()