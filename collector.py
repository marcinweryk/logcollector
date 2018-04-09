import os, fnmatch

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
    sizeinmb = 

result = find('*.log', 'C:\impact360')
listoffiles = '\n'.join(map(str,result))
#print('\n'.join(map(str,result)))
for files in result:
    print('File: ', files, os.path.getsize(files))

