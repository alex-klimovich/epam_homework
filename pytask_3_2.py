import urllib
import multiprocessing
from HTMLParser import HTMLParser
from pprint import pprint
from mock import patch


def file_opener(url):
    if url == 'https://github.com':
        return open('github.html')
    else:
        return open('google.html')


# old-style class
class CustomHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self._links = []

    def feed(self, data):
        HTMLParser.feed(self, data)
        return self._links

    # override
    def handle_starttag(self, tag, attrs):
        if tag == "a":
            for name, value in attrs:
                if name == "href" and value.startswith('http'):
                    self._links.append(value)

    # implement method of abstract class
    def error(self, message):
        HTMLParser.error(self, message)

    @property
    def links(self):
        return self._links


@patch('urllib.urlopen', file_opener)
def find_links_from_url(url):
    parser = CustomHTMLParser()
    parser.feed(urllib.urlopen(url).read())
    return (url, parser.links)


def links_finder(urls):
    p = multiprocessing.Pool(len(urls) if len(urls) < 9 else None)
    res = p.map(find_links_from_url, urls)
    return dict(res)


if __name__ == "__main__":
    links = links_finder(["https://www.google.by", "https://github.com"])
    pprint(links)
