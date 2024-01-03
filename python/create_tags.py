from create_blog_list import create_list_html

def get_tags(blogs):
    tags = {}

    for blog in blogs:
        for tag in blog.tags:
            if tag not in tags:
                tags[tag] = []

            tags[tag].append(blog)

    return tags

def write_tag_files(blogs):
    tags = get_tags(blogs)

    for tag_key in tags:
        f = open("../html/tags/"+tag_key, "w")
        f.write(create_list_html(title = tag_key, blog_list = tags[tag_key]))