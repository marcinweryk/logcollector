import os, fnmatch
import time

# this will show the first match for search
def find(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)

# this will show all matches for search
def find_all(name, path):
    result = []
    for root, dirs, files in os.walk(path):
        if name in files:
            result.append(os.path.join(root, name))
    return result

# this will show match for patern

def find(pattern, path):
    result = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                result.append(os.path.join(root, name))
    return result

def convertbyte(sizeinbbyte):
    sizeinmb = sizeinbbyte/1024/1024
    return sizeinmb

#find all the log in the directory
result = find('*.log*', 'C:\mytestdirectory')

# Some tests for single file below
#listoffiles = '\n'.join(map(str,result))
#updresult = ' '.join(map(str,result))
#print(updresult, os.path.getsize(updresult))

#open fiel to save
f = open('logfileslist.txt','w')

# all results per line are saved in the file
for files in result:
    print('File: ', files, ("%.2f" % convertbyte(os.path.getsize(files))), 'MB', '( Last modified:' ,time.ctime(os.path.getmtime(files)),')')
    filelinef = ("File: {}, {} MB, Last modified: {} \n".format(files,("%.2f" % convertbyte(os.path.getsize(files))), time.ctime(os.path.getmtime(files)) ))
    f.write(str(filelinef))
f.close()





