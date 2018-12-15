#!python
print("content-type:text/html; charset:utf-8\n")
print()

import cgi, os, view

listStr=view.mklist()

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
  <form action="process_create.py" method="post">
    <p><input type="text" placeholder="title" name="title"></p>
    <p><textarea rows="10" placeholder="description" name="description"></p>
    <p><input type="submit"></p>
</body>
</html>
'''.format(listStr=listStr)
