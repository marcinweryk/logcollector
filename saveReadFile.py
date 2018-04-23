# a very simple Tkinter editor to show file read/write dialog

from tkinter import *
from tkinter import filedialog


class App(object):
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()
        self.text = Text()
        self.text.pack()

        menu = Menu(master)
        root.config(menu=menu)
        # file menu
        filemenu = Menu(menu, tearoff=0)
        menu.add_cascade(label="File", menu=filemenu)
        filemenu.add_command(label="New")
        filemenu.add_command(label="Open", command=self.file_open)
        filemenu.add_command(label="Save", command=self.file_save)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.do_exit)

    def file_open(self):
        """open a file to read"""
        # optional initial directory (default is current directory)
        initial_dir = "C:\Temp"
        # the filetype mask (default is all files)
        mask = \
            [("Text and Python files", "*.txt *.py *.pyw"),
             ("HTML files", "*.htm"),
             ("All files", "*.*")]
        fin = filedialog.askopenfile(initialdir=initial_dir, filetypes=mask, mode='r')
        text = fin.read()
        if text != None:
            self.text.delete(0.0, END)
            self.text.insert(END, text)

    def file_save(self):
        """get a filename and save the text in the editor widget"""
        # default extension is optional, here will add .txt if missing
        fout = filedialog.asksaveasfile(mode='w', defaultextension=".txt")
        text2save = str(self.text.get(0.0, END))
        fout.write(text2save)
        fout.close()

    def do_exit(self):
        root.destroy()


root = Tk()
root.title("a very simple editor")
app = App(root)
root.mainloop()