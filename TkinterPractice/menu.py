from tkinter import *
from tkinter import messagebox
def onClick(label):
    print('hi')
    #messagebox.showinfo("Message","You Clicked "+label)
window=Tk()

menu=Menu(window)
filemenu = Menu(menu, tearoff=0)
filemenu.add_cascade(label="File",menu=menu)
filemenu.add_command(label="New Window", command=onClick("New Window"))
filemenu.add_command(label="New File",command=onClick("New File"))
filemenu.add_command(label="Open File",command=onClick("Open File"))
filemenu.add_command(label="Open Folder",command=onClick("Open Folder"))
filemenu.add_command(label="Add Project Folder",command=onClick("Add Project Folder"))
filemenu.add_command(label="Reopen Project",command=onClick("Reopen Project"))
filemenu.add_command(label="Report Last Item",command=onClick("Report Last Item"))
filemenu.add_seperator()

filemenu.add_command(label="Save",command=onClick("Save"))
filemenu.add_command(label="Save As",command=onClick("Save As"))
filemenu.add_command(label="Save All",command=onClick("Save All"))
filemenu.add_seperator()
filemenu.add_command(label="Close Tab",command=onClick("Close Tab"))
filemenu.add_command(label="Close Pane",command=onClick("Close Window"))
filemenu.add_command(label="Close Window",command=onClick(label))
filemenu.add_seperator()
filemenu.add_command(label="Quit",command=onClick("Quit"))
filemenu.add_command(label="Close All Tabs",command=onClick("Close All Tabs"))
window.config(menu=menu)
window.mainloop()
