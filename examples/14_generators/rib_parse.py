# wget https://github.com/intrig-unicamp/ALTO-as-a-Service/raw/master/IXP-PTT-BR/20141208/PTTMetro-LG-Dataset/IPv4/processed/rib.table.lg.ba.ptt.br-BGP.csv.gz
# gunzip rib.table.lg.ba.ptt.br-BGP.csv.gz

import csv
from collections import namedtuple
from typing import Iterator, Iterable, Tuple, NamedTuple, List

# "status","network","netmask","nexthop","metric","locprf","weight","path","origin"
# "*","1.0.0.0","24","200.219.145.45",NA,NA,0,"28135 18881 3549 15169","i"
# "*>","1.0.0.0","24","200.219.145.23",NA,NA,0,"53242 7738 15169","i"
# "*","1.0.4.0","24","200.219.145.45",NA,NA,0,"28135 18881 3549 1299 7545 56203","i"
# "*>","1.0.4.0","24","200.219.145.23",NA,NA,0,"53242 12956 174 7545 56203","i"

Route = namedtuple(
    "Route",
    [
        "status",
        "network",
        "netmask",
        "nexthop",
        "metric",
        "locprf",
        "weight",
        "path",
        "origin",
    ],
)


def read_csv(filename: str) -> Iterator[Tuple[int, List[str]]]:
    with open(filename) as f:
        reader = csv.reader(f)
        for index, line in enumerate(reader, 1):
            print(index, line)
            yield index, line


def create_route(
    iterable: Iterable[Tuple[int, List[str]]]
) -> Iterator[Tuple[int, Route]]:
    for index, line in iterable:
        yield index, Route(*line)


def filter_by_nexthop(iterable, nexthop):
    for index, route in iterable:
        if route.nexthop == nexthop:
            yield index, route


def filter_by_netmask(iterable, mask):
    for index, route in iterable:
        if route.netmask == mask:
            yield index, route


if __name__ == "__main__":
    result = read_csv("rib.table.lg.ba.ptt.br-BGP.csv")
    routes = create_route(result)
    nhop_23 = filter_by_nexthop(routes, "200.219.145.23")
    mask_22 = filter_by_netmask(nhop_23, "22")
