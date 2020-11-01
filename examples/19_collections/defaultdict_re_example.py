import re
from pprint import pprint
from collections import defaultdict


def get_ip_from_cfg(filename):
    result = defaultdict(list)
    regex = (r"^interface (?P<intf>\S+)"
             r"|address (?P<ip>\S+) (?P<mask>\S+)")

    with open(filename) as f:
        for line in f:
            match = re.search(regex, line)
            if match:
                if match.lastgroup == "intf":
                    intf = match.group(match.lastgroup)
                elif match.lastgroup == "mask":
                    #if not intf in result:
                    #    result[intf] = []
                    # result.setdefault(intf, [])
                    result[intf].append(match.group("ip", "mask"))
    return result


if __name__ == "__main__":
    pprint(get_ip_from_cfg("config_r2.txt"))
