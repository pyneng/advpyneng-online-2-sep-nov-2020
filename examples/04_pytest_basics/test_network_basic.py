import subprocess
import pytest
from netmiko import ConnectHandler
import re


def parse_cdp_n(output):
    regex = r"^(\S+) +\S+ +\S+ +\d+"
    return re.findall(regex, output, re.MULTILINE)


def parse_sh_ip_int_br(output):
    regex = r"^(\S+) +[\d.]+"
    return re.findall(regex, output, re.MULTILINE)


def send_show_command(device, command):
    print(f"Connect {device['host']}")
    with ConnectHandler(**device) as ssh:
        ssh.enable()
        result = ssh.send_command(command)
    return result


def ping_ip(ip):
    result = subprocess.run(f"ping -c 1 {ip}", shell=True, stdout=subprocess.PIPE)
    return result.returncode == 0


ip_list = ["192.168.100.1", "192.168.100.2", "192.168.100.3"]
device = {
    "device_type": "cisco_ios",
    "username": "cisco",
    "password": "cisco",
    "secret": "cisco",
}
devices_params = [{"host": ip, **device} for ip in ip_list]


@pytest.mark.parametrize("ip", ip_list)
def test_ip_reachable(ip):
    assert ping_ip(ip) == True


@pytest.mark.parametrize("device", devices_params)
def test_ospf_enabled(device):
    output = send_show_command(device, "sh ip ospf")
    assert "Routing Process" in output


@pytest.mark.parametrize("device", devices_params)
def test_cdp_n(device):
    output = send_show_command(device, "sh cdp ne")
    neighbors = parse_cdp_n(output)
    print(neighbors)
    assert len(neighbors) != 0


@pytest.mark.parametrize("device", devices_params)
def test_loopback(device):
    output = send_show_command(device, "sh ip int br | i up +up")
    #assert "Loopback0" in output
    assert "Loopback0" in parse_sh_ip_int_br(output)

