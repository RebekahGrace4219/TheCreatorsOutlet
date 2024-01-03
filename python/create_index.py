from create_blog_list import create_list_html

def write_index_file(blogs):
    f = open("../index.html", "w")
    f.write(create_list_html(title = "Blog", blog_list = blogs))
    return