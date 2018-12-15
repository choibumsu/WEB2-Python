#!python
print("content-type:text/html; charset:utf-8\n")
print()

import cgi, os

listStr=''
files = os.listdir('data')
for item in files:
    listStr = listStr + '<li> <a href="index.py?id={name}">{name}</a></li>'.format(name=item)

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
