
def create_header(is_index = False):
        header = "html/" if is_index else ""
        return """
<header>
<a class="home" href="/TheCreatorsOutlet">Home</a>
<nav>
<a href ="https://github.com/RebekahGrace4219">GitHub</a>
<a href = "{header}about-me.html">About Me</a>
<a href = "{header}contact.html">Contact</a>
</nav>
</header>
""".format(header = header)