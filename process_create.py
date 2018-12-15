#!python

import cgi
form=cgi.FiledStorage()
title = form["title"].value
desc = form["description"].value

opened_file=open("data\"+title, 'w')
opened_file.write(desc)
opened_file.close()

print("Location:index.py?id="+title)
print()
