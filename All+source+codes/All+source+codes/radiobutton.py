import tkinter as tk

root = tk.Tk()
root.title("the Radiobutton widget")
root.minsize(300,200)


for text, value in [("Apple", 1),("Banana",2),("grape",3),("strawberry",4),("Olive",5)]:
    tk.Radiobutton(root,text=text, value=value, indicatoron=0).pack()



root.mainloop()