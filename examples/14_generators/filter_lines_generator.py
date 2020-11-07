import re


def read_file(filename):
    with open(filename) as f:
        for index, line in enumerate(f, 1):
            print("read_file", index, line.rstrip())
            yield line


def filter_lines(iterable, regex):
    for line in iterable:
        if re.search(regex, line):
            print("filter_lines", line.rstrip())
            yield line


def convert_to_lower(iterable):
    for line in iterable:
        print("convert_to_lower", line.rstrip())
        yield line.lower()



if __name__ == "__main__":
    file = read_file("config_r1.txt")
    filtered = filter_lines(file, "^interface|^ ip address")
    lower = map(str.lower, filtered)
    lower = (str.lower(line) for line in filtered)

    with open("result.txt", "w") as f:
        for line in lower:
            f.write(line)


