import os

def mkList():
    listStr=''
    files = os.listdir('data')
    for item in files:
        listStr = listStr + '<li> <a href="index.py?id={name}">{name}</a></li>'.format(name=item)
    return listStr
