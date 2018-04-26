import collector
from tkinter import *
from tkinter import filedialog
import traceback
import logging

###################log info #########################
logging.basicConfig(filename='collector.log', level=logging.DEBUG, format='%(message)s %(asctime)s')
logging.info('Started')
############### log start ######################


master = Tk()
master.resizable(FALSE,FALSE)
master.title(string="Log Collector")

scrollbar = Scrollbar(master)
scrollbar.pack(side=RIGHT, fill=Y)

listbox = Listbox(master, width=120, height=20,yscrollcommand=scrollbar.set)
listbox.pack(side=BOTTOM)
listbox.insert(END, "Click search to look for logs")

scrollbar.config(command=listbox.yview)

e = Entry(master)
e.insert(END, "*.log")
e.pack(side=LEFT)
e1 = Entry(master)
e1.insert(END, "c:\FolderName")
e1.pack(side=LEFT)

def searchforme():
    # find all the log type files in the directory
    try:
        result = collector.find(e.get(), e1.get())
        listbox.delete(0,END)
        sizeOfWin = []
        # all results per line are shown on the screen
        for files in result:
            filelinef = ("File: {} | size: {} MB | Last modified: {} \n".format(files,("%.2f" % collector.convertbyte(collector.getsizeoffile(files))), collector.getlastmoddate(files) ))
            listbox.insert(END, filelinef)
            sizeOfWin.append(len(filelinef))
        listbox.config(width=max(sizeOfWin))
    except:
        listbox.insert(END, "No results - Check provided file name and path !")
        logging.exception("Error in the application")

def file_save():
    """get a filename and save the text in the editor widget"""
    # default extension is optional, here will add .txt if missing
    print(listbox.get(ACTIVE))
    result = listbox.get(ACTIVE)
    print(result)
    mask = \
        [("Text files", "*.txt"),
         ("CSV","*.csv"),
         ("All files", "*.*")]
    fout = filedialog.asksaveasfile(mode='w', defaultextension=mask ,filetypes=mask)
    for files in result:
        text2save = ("File: {} | size: {} MB | Last modified: {} \n".format(files,("%.2f" % collector.convertbyte(collector.getsizeoffile(files))), collector.getlastmoddate(files) ))
        fout.write(text2save)
    fout.close()

def do_exit():
    master.destroy()

button1 = Button(text="Search", command=searchforme)
button1.pack(side=LEFT)
menu = Menu(master)
master.config(menu=menu)
# file menu
filemenu = Menu(menu, tearoff=0)
menu.add_cascade(label="Options", menu=filemenu)
filemenu.add_command(label="Save", command=file_save)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=do_exit)
master.protocol("WM_DELETE_WINDOW", master.quit())
mainloop()
###############log ######################
logging.info('Finished')
###############log ######################