import tkinter as tk

root = tk.Tk()
root.title("scrolling through a list")
root.minsize(300,200)

frame = tk.Frame(root, height= 7, width= 10)

l = tk.Listbox(frame, width=15, height= 5, justify="right", selectbackground="red", selectmode="extended")

scroll = tk.Scrollbar(frame, command=l.yview)

l.config(yscrollcommand=scroll.set)

scroll.pack(side ="right", fill="y")

for item in range(15):
    l.insert("end",item)

l.pack()
frame.pack()


root.mainloop()