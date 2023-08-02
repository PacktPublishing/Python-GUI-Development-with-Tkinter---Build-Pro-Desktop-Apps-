import tkinter as tk

root = tk.Tk()
root.title("Let's Make a Menu")
root.minsize(300,200)

mainmenu = tk.Menu(root)

# File Menu starte here

filemenu = tk.Menu(mainmenu,tearoff= 0)

filemenu.add_command(label = "New Text File")
filemenu.add_command(label = "New File")
filemenu.add_command(label = "New Window")
filemenu.add_separator()
filemenu.add_command(label = "Open File")
filemenu.add_command(label = "Open Folder")

# open recnt dropdown starts here
openrecent = tk.Menu(mainmenu)
openrecent.add_command(label="File 1 12/11/23")
openrecent.add_command(label="File 2 11/11/23")
openrecent.add_command(label="File 3 22/11/23")
openrecent.add_command(label="File 4 16/11/23")

filemenu.add_cascade(label="Open Recent", menu = openrecent)

filemenu.add_separator()

filemenu.add_command(label="Exit", command = root.quit)

mainmenu.add_cascade(label="File", menu= filemenu)

#Edit menu start here

editmenu = tk.Menu(mainmenu,tearoff= 0)

editmenu.add_command(label = "undo")
editmenu.add_command(label = "redo")
editmenu.add_separator()
editmenu.add_command(label = "Copy")
editmenu.add_command(label = "Cut ")
editmenu.add_command(label = "Paste")
editmenu.add_separator()
editmenu.add_command(label = "Find")
editmenu.add_command(label = "replace")

mainmenu.add_cascade(label="Edit", menu= editmenu)

#View menu starts here

viewmenu = tk.Menu(mainmenu,tearoff= 0)

viewmenu.add_checkbutton(label = "terminal")
viewmenu.add_checkbutton(label = "explorer")
viewmenu.add_separator()
viewmenu.add_radiobutton(label = "menu")
viewmenu.add_radiobutton(label = "panel ")
viewmenu.add_radiobutton(label = "output")
viewmenu.add_separator()
viewmenu.add_command(label = "problems")
viewmenu.add_command(label = "debug console")

mainmenu.add_cascade(label="View", menu= viewmenu)


root.config(menu= mainmenu)

root.mainloop()