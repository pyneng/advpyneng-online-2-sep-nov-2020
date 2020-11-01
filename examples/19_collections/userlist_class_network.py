from collections import UserList
from collections.abc import Sequence
import ipaddress


class Network(UserList):
    def __init__(self, network):
        hosts = [str(ip) for ip in ipaddress.ip_network(network).hosts()]
        super().__init__(hosts)


class Network(Sequence):
    def __init__(self, network):
        self.hosts = [str(ip) for ip in ipaddress.ip_network(network).hosts()]

    def __getitem__(self, index):
        return self.hosts[index]

    def __len__(self):
        return len(self.hosts)
