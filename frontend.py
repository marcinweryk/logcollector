import collector
from tkinter import *

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


def save():
    # find all the log type files in the directory
    result = collector.find('*.log', 'C:\mytestdirectory')
    listbox.delete(0, END)
    # open file to save the results of search
    f = open('logfileslist.txt', 'w')

    # all results per line are saved in the file
    for files in result:
        filelinef = ("File: {} | size: {} MB | Last modified: {} \n".format(files,("%.2f" % collector.convertbyte(collector.getsizeoffile(files))), collector.getlastmoddate(files) ))
        f.write(str(filelinef))
    listbox.insert(END, "Saved file logfileslist.txt")
    f.close()

button1 = Button(text="Search", command=searchforme)
button1.pack(side=LEFT)
button2 = Button(text="Save", command=save)
button2.pack(side=LEFT)
master.protocol("WM_DELETE_WINDOW", master.quit())
mainloop()