import tkinter as tk

root = tk.Tk()
root.title("My Toplevel Application")
root.minsize(300,200)

toplevel = None

def top():
    global toplevel
    toplevel = tk.Toplevel(root)
    label = tk.Label(toplevel, text="Terms And Conditions!").pack()
    terms = tk.Message(toplevel, text="This is an greement that stands as the terms and conditions of the metabrains. Here you promise to learn consisitently in order to become a world changing enfgineer tomorrow. set yourself a daily goall to afvance step by step, this will be a forward wove toward your dreams", width=300).pack()
    radio = tk.Radiobutton(toplevel,text="I agree", command=agree, state="normal", value=1).pack()
    radio = tk.Radiobutton(toplevel,text="I desagree", command=root.quit,state="normal").pack()

def agree():
    global toplevel
    tk.Label(root, text=" Good Choice").pack()
    toplevel.destroy()



btn = tk.Button(root, text="Install", command= top).pack()

root.mainloop()