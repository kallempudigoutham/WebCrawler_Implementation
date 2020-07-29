from html.parser import HTMLParser
from urllib import parse


# Class inherits HTMLParser
class LinkFinder(HTMLParser):
    def __init__(self):
        super().__init__()

    def handle_starttag(self, tag, attrs):
        print(tag)

    def error(self, message):
        pass


finder = LinkFinder()
finder.feed('<html><head><title>Test</title></head>'
            '<body><h1>Parse Me!</h1></body></html>')
