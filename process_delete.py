#!python

import cgi
form=cgi.FiledStorage()
linkId=form["linkId"].value

os.remove('data\'+linkId)

print("Location:index.py")
print()
