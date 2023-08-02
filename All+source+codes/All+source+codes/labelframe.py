import tkinter as tk

root = tk.Tk()
root.title("Grouping widget with Labelframe")
root.minsize(300,200)

labelframe= tk.LabelFrame(root, text="Login")
labelframe.pack()

label_Email = tk.Label(labelframe, text="Email: ")
email_entry = tk.Entry(labelframe)
label_password = tk.Label(labelframe, text="Password: ")
password_entry = tk.Entry(labelframe)

label_Email.grid(column= 0, row= 0)
email_entry.grid(column= 1, row= 0)
label_password.grid(column= 0, row= 1)
password_entry.grid(column= 1, row= 1)


root.mainloop()