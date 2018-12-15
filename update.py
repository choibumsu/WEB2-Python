#!python
print("content-type:text/html; charset:utf-8\n")
print()

import cgi, os, view

listStr=view.mklist()

form = cgi.FieldStorage()
if 'id' in form:
    linkId=form["id"].value
    description = open("data\"+linkId, 'r').read()
else:
    linkId="Bumsu's Home"
    description = "This is a <u>Bumsu's Home</u>"

print('''
<!doctype html>
<html>
<head>
  <title>bumsu_home</title>
  <meta charset="uft-8">
</head>
<body>
  <h1> <a href="index.py" title="home">Bumsu_Home</a></h1>
  <ol>{listStr}</ol>
  <a href="create.py" title="create">create</a>
  <form action="process_update.py" method="post">
    <p><input type="hidden" name="linkId" value={default_title}></p>
    <p><input type="text" placeholder="title" name="title" value={default_title}></p>
    <p><textarea rows="10" placeholder="description" name="description" value={default_desc}></p>
    <p><input type="submit"></p>
</body>
</html>
'''.format(listStr=listStr, default_title=linkId, default_desc=description)
