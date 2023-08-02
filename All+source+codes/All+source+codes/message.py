import tkinter as tk

root = tk.Tk()
root.title("Multiple lines with Message")
root.minsize(300,200)


tk.Message(root,text="we can say that a Message widget is just like the label widget just that is displays lontg text by default in multiple lines, it is kind of obsolete now but canstill help in some cases", bg="royalblue", width=200, justify="center", relief="raised").pack()


root.mainloop()