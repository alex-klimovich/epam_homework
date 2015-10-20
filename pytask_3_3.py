import re
import multiprocessing
from pprint import pprint

# COUNT_LINES_PER_THREAD = 100


def process_grep(regex, lines):
    if regex.search(lines):
        return lines


def grep(regex_string, file_path):
    regex = re.compile(regex_string)
    p = multiprocessing.Pool()
    f = open(file_path)
    res = []
    for n, line in enumerate(f.readlines(), start=1):
        res.append((n, p.apply(process_grep, args=(regex, line))))
    return [_ for _ in res if _[1]]


if __name__ == "__main__":
    lines = grep(r"rsyslogd", "messages.log")
    pprint(lines)
