import re
from typing import List, Tuple


def parse_sh_cdp_neighbors(command_output: str) -> List[Tuple[str, ...]]:
    regex = re.compile(
        r"(?P<r_dev>\w+) +(?P<l_intf>\S+ \S+)"
        r" +\d+ +[\w ]+ +\S+ +(?P<r_intf>\S+ \S+)"
    )
    connect_list = []
    match_l_dev = re.search(r"(\S+)[>#]", command_output)
    if match_l_dev:
        l_dev = match_l_dev.group(1)
    for match in regex.finditer(command_output):
        neighbor = (l_dev, *match.group("l_intf", "r_dev", "r_intf"))
        connect_list.append(neighbor)
    return connect_list
