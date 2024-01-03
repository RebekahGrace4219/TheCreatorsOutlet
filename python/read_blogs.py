import os
import json
from create_header import create_header
PATH_TO_BLOG_POSTS = "../website_info/blogs/"

class Blog:
    def __init__(self, file_path):
        self.file_path = file_path

        file = json.load(open(PATH_TO_BLOG_POSTS + file_path))
        self.year = file["Date"]["Year"]
        self.month = file["Date"]["Month"]
        self.day = file["Date"]["Day"]

        self.title = file["Title"]
        self.signOff = file["SignOff"]
        self.signedName = file["SignedName"]
        self.route = file["Route"]
        self.tags = file["Tags"]

        self.body = file["Body"]

        self.full_html = self.create_full_html()

    def expand_date(self, number):
        if int(number) <= 9:
            return "0"+str(number)
        return str(number)

    def comparator(self):
        return str(self.year) + self.expand_date(self.month) + self.expand_date(self.day)

    def format_date(self):
        months = ["Jan", "Feb", "Mar","Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        return months[int(self.month)-1]+ " "+ str(self.day)+", "+str(self.year)

    def format_body(self):
        body_text = ""
        for i in range(1, len(self.body)+1):
            key = "P"+str(i)
            body_part = self.body[key]

            if body_part["Type"] == "Text":
                body_text += "<p>{body_text}</p>\n".format(body_text = body_part["Content"])

        return body_text

    def format_tags(self):
        tag_text = ""
        for tag in self.tags:
            tag_text += "<li>\n\t<a href = \"../tags/{tag}\">{tag}</a>\n</li>".format(tag = tag)

        return tag_text

    def create_full_html(self):
        return """
<html>
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel="stylesheet" href="css/style.css" type="text/css">
        <title>{title}</title>
    </head>
    <body>
        {header}
        <div class = "blogpost">
            <h1>{title}</h1>
            <h2>{date}</h2>
            <ul>
{tags}
            </ul>
            <div class = "blogpostbody">
{body}
            </div>

            <div class = "blogpostsignoff">
                <p>{signOff}</p>
                <p>{signedName}</p>
            </div>
        </div>
    </body>
<html>
""".format(header = create_header(), title = self.title, date = self.format_date(), tags = self.format_tags(), body = self.format_body(), signOff = self.signOff, signedName=self.signedName)

def get_blog_info():
    blog_files = os.listdir(PATH_TO_BLOG_POSTS)
    blog_objs = []

    for blog_file in blog_files:
        blog = Blog(blog_file)
        blog_objs.append(blog)

    blog_objs.sort(key=lambda x: x.comparator())
    return blog_objs