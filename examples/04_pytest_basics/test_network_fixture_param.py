import subprocess
import pytest
from netmiko import ConnectHandler
import re
import yaml


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
        result = ssh_connection.send_command(command)
    return result


def ping_ip(ip):
    result = subprocess.run(f"ping -c 1 {ip}", shell=True, stdout=subprocess.PIPE)
    return result.returncode == 0


with open("devices.yaml") as f:
    devices_params = yaml.safe_load(f)
ip_list = [d["host"] for d in devices_params]


@pytest.fixture(params=devices_params, scope="session", ids=ip_list)
def ssh_connection(request):
    ssh = ConnectHandler(**request.param)
    ssh.enable()
    print(f"\n\n>>>>> Подключение {request.param['host']}")
    yield ssh
    print(f"\n\n>>>>> Закрываю сессию {request.param['host']}")
    ssh.disconnect()


def test_ospf_enabled(ssh_connection):
    output = ssh_connection.send_command("sh ip ospf")
    assert "Routing Process" in output


def test_cdp_n(ssh_connection):
    output = ssh_connection.send_command("sh cdp ne")
    neighbors = parse_cdp_n(output)
    # print(neighbors)
    assert len(neighbors) != 0


def test_loopback(ssh_connection):
    output = ssh_connection.send_command("sh ip int br | i up +up")
    # assert "Loopback0" in output
    assert "Loopback0" in parse_sh_ip_int_br(output)


def test_ping_isp(ssh_connection):
    output = ssh_connection.send_command("ping 192.168.100.100")
    assert "Success rate is 100 percent" in output
