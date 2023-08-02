import tkinter as tk
import random

root = tk.Tk()
root.title("Bitmaps")
root.minsize(300,200)

def on_click():
    bmp = ["error","gray25", "gray50","gray75","gray12","hourglass","questhead","info", "warning","question"]
    if btn['bitmap'] in bmp:
        i = random.randint(0,len(bmp)-1)
        btn.config(bitmap=bmp[i])
        label.config(text=bmp[i].upper())

label = tk.Label(root,text="ERROR")
btn = tk.Button(root, text="Raised", relief="raised",bitmap="error", command=on_click)
label.pack()
btn.pack()

root.mainloop()