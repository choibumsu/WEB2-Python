#!python
print("content-type:text/html; charset:utf-8\n")
print()

import cgi, os, view

listStr=view.mklist()

form = cgi.FieldStorage()
if 'id' in form:
    linkId=form["id"].value
    description = open("data\"+linkId, 'r').read()
    update_link = '<a href="update.py?id={}" title="update">update</a>'.format(linkId)
    delete_action='''
    <form action="process_delete.py" mehtod="post">
        <input type="hidden" name="linkId" value="{}">
        <input type="submit" value="delete">
    </form>
    '''.format(linkId)
else:
    linkId="Bumsu's Home"
    description = "This is a <u>Bumsu's Home</u>"
    update_link=''
    delete_action=''

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
  {update_link}
  {delete_action}
  <h2>{title}</h2>
  <p>{desc}</p>
</body>
</html>
'''.format(title=linkId), desc=description, listStr=listStr, update_link = update_link, delete_action=delete_action)
