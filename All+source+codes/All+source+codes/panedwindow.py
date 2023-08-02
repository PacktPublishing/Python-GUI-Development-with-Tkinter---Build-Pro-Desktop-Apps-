import tkinter as tk

root = tk.Tk()
root.title("Dividing with panes")
root.minsize(300,200)

panedwindow = tk.PanedWindow(root, bg="yellow", orient="vertical", width=200,)

panedwindow.pack()

l1 = tk.Label(panedwindow, text="Pane 1")
panedwindow.add(l1)
l2 = tk.Label(panedwindow, text="Pane 2")
panedwindow.add(l2)
l3 = tk.Label(panedwindow, text="Pane 3")
panedwindow.add(l3)

root.mainloop()