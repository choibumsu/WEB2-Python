#!python

import cgi
form=cgi.FiledStorage()
linkId = form["linkId"].value
title = form["title"].value
desc = form["description"].value

opened_file=open("data\"+linkId, 'w')
opened_file.write(desc)
opened_file.close()

os.rename("data\"+linkId,"data\"+title)

print("Location:index.py?id="+title)
print()
