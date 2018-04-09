import collector


#find all the log type files in the directory
result = collector.find('*.log', 'C:\mytestdirectory')

#open file to save the results of search
f = open('logfileslist.txt','w')

# all results per line are saved in the file
for files in result:
    #print("File: {}, {} MB, Last modified: {}".format(files,("%.2f" % collector.convertbyte(collector.getsizeoffile(files))), collector.getlastmoddate(files) ))
    filelinef = ("File: {}, {} MB, Last modified: {} \n".format(files,("%.2f" % collector.convertbyte(collector.getsizeoffile(files))), collector.getlastmoddate(files) ))
    f.write(str(filelinef))
#close the file
f.close()
