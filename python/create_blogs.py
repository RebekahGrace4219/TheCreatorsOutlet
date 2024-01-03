def write_blog_files(blogs_info):
    for blog in blogs_info:
        file = open("../html/blogs/"+blog.route, "w")
        file.write(blog.full_html)
