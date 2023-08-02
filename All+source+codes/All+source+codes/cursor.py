import tkinter as tk
import random

root = tk.Tk()
root.title("Cursor Appearance on Widget")
root.minsize(300,200)

def on_click():
    cursors = ["arrow","circle", "clock","cross","dotbox","exchange","fleur","heart", "man","mouse"]
    if btn['cursor'] in cursors:
        i = random.randint(0,len(cursors)-1)
        btn.config(cursor=cursors[i])
        label.config(text=cursors[i].upper())

label = tk.Label(root,text="ARROW")
btn = tk.Button(root, text="Raised", relief="raised",cursor="arrow", command=on_click)
label.pack()
btn.pack()

root.mainloop()