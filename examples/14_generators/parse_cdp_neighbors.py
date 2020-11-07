import re
from pprint import pprint
from typing import Iterator


def read_by_neighbor(filename: str) -> Iterator[str]:
    with open(filename) as f:
        line = ""
        while True:
            while "Device ID" not in line:
                line = f.readline()
            neighbor = line
            for line in f:
                if "-------------------------" in line:
                    break
                neighbor += line
            yield neighbor
            line = f.readline()
            if not line:
                return None


def parse_cdp(neighbor):
    regex = (
        r"Device ID: (\S+).+?"
        r" +IP address: (?P<ip>\S+).+?"
        r"Cisco IOS Software, .+?, Version (?P<ios>\S+),"
    )
    match = re.search(regex, neighbor, re.DOTALL)
    if match:
        device = match.group(1)
        result = {device: match.groupdict()}
        return result


if __name__ == "__main__":
    data = read_by_neighbor("sh_cdp_neighbors_detail.txt")
    for n in data:
        pprint(parse_cdp(n), width=120)
