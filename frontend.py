import collector
from tkinter import *

master = Tk()

listbox = Listbox(master, width=120, height=20)
listbox.pack()

listbox.insert(END, "List of log files:")


def searchforme():
    # find all the log type files in the directory
    result = collector.find('*.log', 'C:\mytestdirectory')

    # open file to save the results of search
    f = open('logfileslist.txt', 'w')

    # all results per line are saved in the file
    for files in result:
        filelinef = ("File: {} | size: {} MB | Last modified: {} \n".format(files,("%.2f" % collector.convertbyte(collector.getsizeoffile(files))), collector.getlastmoddate(files) ))
        f.write(str(filelinef))
        listbox.insert(END, filelinef)
    f.close()

button1 = Button(text="Search", command = searchforme)
button1.pack()

mainloop()