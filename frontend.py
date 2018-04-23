import collector
from tkinter import *
from tkinter import filedialog

master = Tk()
master.resizable(FALSE,FALSE)
master.title(string="Log Collector")

scrollbar = Scrollbar(master)
scrollbar.pack(side=RIGHT, fill=Y)

listbox = Listbox(master, width=120, height=20,yscrollcommand=scrollbar.set)
listbox.pack(side=BOTTOM)
listbox.insert(END, "Click search to look for logs")

scrollbar.config(command=listbox.yview)

def searchforme():
    # find all the log type files in the directory
    result = collector.find('*.log', 'C:\mytestdirectory')
    listbox.delete(0,END)
    # all results per line are shown on the screen
    for files in result:
        filelinef = ("File: {} | size: {} MB | Last modified: {} \n".format(files,("%.2f" % collector.convertbyte(collector.getsizeoffile(files))), collector.getlastmoddate(files) ))
        listbox.insert(END, filelinef)

def file_save():
    """get a filename and save the text in the editor widget"""
    # default extension is optional, here will add .txt if missing
    #result = collector.find('*.log', 'C:\mytestdirectory')
    print(listbox.get(ACTIVE))
    result = listbox.get(ACTIVE)
    print(result)
    mask = \
        [("Text files", "*.txt"),
         ("All files", "*.*")]
    fout = filedialog.asksaveasfile(mode='w', defaultextension=mask ,filetypes=mask)
    for files in result:
        text2save = ("File: {} | size: {} MB | Last modified: {} \n".format(files,("%.2f" % collector.convertbyte(collector.getsizeoffile(files))), collector.getlastmoddate(files) ))
        fout.write(text2save)
    fout.close()

def do_exit():
    master.destroy()

menu = Menu(master)
master.config(menu=menu)
# file menu
filemenu = Menu(menu, tearoff=0)
menu.add_cascade(label="Options", menu=filemenu)
filemenu.add_command(label="Search", command=searchforme)
filemenu.add_separator()
filemenu.add_command(label="Save", command=file_save)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=do_exit)

#button1 = Button(text="Search", command=searchforme)
#button1.pack(side=LEFT)
master.protocol("WM_DELETE_WINDOW", master.quit())
mainloop()