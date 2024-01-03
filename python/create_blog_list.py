from create_header import create_header

def create_blog_list(title, blogs):
    string = "<h1>{title}</h1><ul>".format(title = title)
    for blog in blogs:
        string += """
<li class = "blogentry">
    <div class = "date"><p>{day}.{month}.{year}<p></div>
    <div class = "blogtitle"><a href = "https://rebekahgrace4219.github.io/TheCreatorsOutlet/html/blogs/{route}.html">{title}</a></div>
</li>
""".format(day = blog.day, month = blog.month, year = blog.year, route = blog.route, title = blog.title)

    string += "</ul>"

    return string

def create_list_html(title, blog_list):
    head = """
<html>
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="https://rebekahgrace4219.github.io/TheCreatorsOutlet/style.css" type="text/css">
    <title>{title}</title>
  </head>
  <body>
""".format(title = title)

    bottom = "</body></html>"

    return head + create_header() + create_blog_list(title, blog_list) + bottom