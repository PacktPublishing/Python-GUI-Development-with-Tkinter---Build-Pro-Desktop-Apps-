import tkinter as tk
import random

root = tk.Tk()
root.title("Widgets with Reliefs")
root.minsize(300,200)

def relief():
    rel = ["raised","sunken", "flat","groove","ridge"]
    if btn['relief'] in rel:
        i = random.randint(0,4)
        btn.config(relief =rel[i])
        btn.config(text=rel[i])

btn = tk.Button(root, text="Raised", relief="raised", command=relief)
btn.pack()

root.mainloop()