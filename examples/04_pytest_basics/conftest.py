import yaml
import pytest
from netmiko import ConnectHandler


@pytest.fixture(scope="session")
def templates(tmpdir_factory):
    pass



@pytest.fixture()
def topology_with_dupl_links():
    topology = {
        ("R1", "Eth0/0"): ("SW1", "Eth0/1"),
        ("R2", "Eth0/0"): ("SW1", "Eth0/2"),
        ("R2", "Eth0/1"): ("SW2", "Eth0/11"),
        ("R3", "Eth0/0"): ("SW1", "Eth0/3"),
        ("R3", "Eth0/1"): ("R4", "Eth0/0"),
        ("R3", "Eth0/2"): ("R5", "Eth0/0"),
        ("SW1", "Eth0/1"): ("R1", "Eth0/0"),
        ("SW1", "Eth0/2"): ("R2", "Eth0/0"),
        ("SW1", "Eth0/3"): ("R3", "Eth0/0"),
    }
    return topology

@pytest.fixture()
def normalized_topology_example():
    normalized_topology = {
        ("R1", "Eth0/0"): ("SW1", "Eth0/1"),
        ("R2", "Eth0/0"): ("SW1", "Eth0/2"),
        ("R2", "Eth0/1"): ("SW2", "Eth0/11"),
        ("R3", "Eth0/0"): ("SW1", "Eth0/3"),
        ("R3", "Eth0/1"): ("R4", "Eth0/0"),
        ("R3", "Eth0/2"): ("R5", "Eth0/0"),
    }
    return normalized_topology


@pytest.fixture(scope="session")
def device_example():
    r1 = {
        "device_type": "cisco_ios",
        "host": "192.168.100.1",
        "username": "cisco",
        "password": "cisco",
        "secret": "cisco",
    }
    return r1



@pytest.fixture(scope="session")
def ssh_connection(device_example):
    # SETUP
    print(f"\nПодключаемся к {device_example['host']}\n")
    ssh = ConnectHandler(**device_example)
    ssh.enable()
    yield ssh
    # TEARDOWN
    ssh.disconnect()
    print(f"\nЗакрыли сессию {device_example['host']}\n")


def pytest_addoption(parser):
    parser.addoption(
        "--ip-list", nargs='+', help="IP list"
    )


@pytest.fixture
def ip_list(request):
    return request.config.getoption("--ip-list")
