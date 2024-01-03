from create_header import create_header

head = """
<html>
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="/style.css" type="text/css">
    <title>Blog</title>
  </head>
  <body>



"""

bottom = "</body></html>"

def write_index_file(blogs):
    f = open("../index.html", "w")
    f.write(head + create_header() + bottom)
    return