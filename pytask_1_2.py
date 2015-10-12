from functools import wraps
import urllib2
import json
import mock


def urlopen(url):
    if url == "http://www.reddit.com/r/golang.json":
        return open("golang.json")
    else:
        return open("python.json")


@mock.patch('urllib2.urlopen', urlopen)
def reddit(url):
    """
    >>> reddit("http://www.reddit.com/r/python.json").__name__
    'reddit'
    """
    data = urllib2.urlopen(url).read()
    py_data = json.loads(data)

    @wraps(reddit)
    def wrapper():
        for _ in py_data["data"]["children"]:
            yield _["data"]["title"]

    return wrapper


python = reddit("http://www.reddit.com/r/python.json")
golang = reddit("http://www.reddit.com/r/golang.json")

for title in python():
    print repr(title)

for title in golang():
    print title
