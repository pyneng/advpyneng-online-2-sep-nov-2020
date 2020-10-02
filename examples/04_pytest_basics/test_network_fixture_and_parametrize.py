import subprocess
import pytest
from netmiko import ConnectHandler
import re
import yaml


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


@pytest.mark.parametrize("route", ["10.1.1.0 255.255.255.0", "192.168.101.0 255.255.255.0"])
def test_routes(ssh_connection, route):
    output = ssh_connection.send_command(f"sh ip route {route}")
    assert "Routing entry for" in output

