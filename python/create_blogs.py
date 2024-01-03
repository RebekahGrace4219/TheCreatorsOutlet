def write_blog_files(blogs_info):
    for blog in blogs_info:
        file = open("../html/blogs/"+blog.route+".html", "w")
        file.write(blog.full_html)
