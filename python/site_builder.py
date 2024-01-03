from python.create_blogs import get_blog_info, write_blog_files
from python.create_index import write_index_file
from python.create_tags import write_tag_files

blogs_info = get_blog_info()

write_blog_files(blogs_info)
write_index_file(blogs_info)
write_tag_files(blogs_info)
