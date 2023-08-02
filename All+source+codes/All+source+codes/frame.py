import tkinter as tk

root = tk.Tk()
root.title("widgets in window with Frame")
root.minsize(300,200)

frame = tk.Frame(root, bg="pink", height= 400, width=400)

label = tk.Label(frame, text = " label in tkinter is use to display text and images and it is widely used through put the tkinter application and i will advice all developers to use this widget", bg= "lightgreen" , font="calibri", wraplength=
300).pack()

for text, value in [("Apple", 1),("Banana",2),("grape",3),("strawberry",4),("Olive",5)]:
    tk.Radiobutton(frame,text=text, value=value, indicatoron=0, width=20).pack()


frame.pack()


root.mainloop()