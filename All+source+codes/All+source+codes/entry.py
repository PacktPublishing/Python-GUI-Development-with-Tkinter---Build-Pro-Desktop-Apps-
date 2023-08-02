import tkinter as tk

root = tk.Tk()
root.title("Entry Widget")

label = tk.Label(root, text="Name: ")
entry = tk.Entry(root)

entry.insert(0, "The Metabrains!")
entry.config(state="disabled")

label.pack()
entry.pack()




root.mainloop()