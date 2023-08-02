import tkinter as tk

root = tk.Tk()
root.title("Label")

label = tk.Label(root, text = " label in tkinter is use to display text and images and it is widely used through put the tkinter application and i will advice all developers to use this widget", bg= "lightgreen" , font="calibri", wraplength=
500)

label.pack()

root.mainloop()