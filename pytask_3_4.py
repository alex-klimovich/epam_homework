from pprint import pprint


class MapReduce(object):
    # TODO: implement MapReduce
    pass


def words_counter(path, ext=None, ignored=None, minlen=None):
    # TODO: get file list
    pass

    # TODO: filter file list
    pass


if __name__ == "__main__":
    exclude = ["if", "else", "on", "at"]
    words = words_counter('/home/keda',
                          ext=["py", "txt"],
                          ignored=exclude,
                          minlen=2)
    pprint(words)
