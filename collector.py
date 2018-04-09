import os, fnmatch
import time

# this will show the first match for specific search
def find(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)

# this will show all matches for specific search
def find_all(name, path):
    result = []
    for root, dirs, files in os.walk(path):
        if name in files:
            result.append(os.path.join(root, name))
    return result

# this will show match for specific patern
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

def getsizeoffile(file):
    sizeoffile = os.path.getsize(file)
    return sizeoffile

def getlastmoddate(file):
    lastmodtime = time.ctime(os.path.getmtime(file))
    return lastmodtime


