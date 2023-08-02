import tkinter as tk
from tkinter.font import Font

root = tk.Tk()
root.title("Change text Appearance with Fonts")
root.minsize(300,200)
#create a neaw font
font1 = Font(
    family="calibri",
    size=14,
    weight = "bold",
    slant="roman",
    underline=0,
    overstrike=0
)

#create a neaw font
font2 = Font(
    family="courier",
    size=14,
    weight = "bold",
    slant="roman",
    underline=1,
    overstrike=0
)
tk.Label(root, text="hello tkinter", font=font1).pack()
tk.Label(root, text="hello tkinter", font=font2).pack()


root.mainloop()