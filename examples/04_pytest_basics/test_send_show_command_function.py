from send_command_functions import (
    send_show_command,
    send_config_commands,
    parse_cdp_n,
    send_show_to_devices,
)
from netmiko import ConnectHandler
import pytest


@pytest.mark.parametrize("ipaddress", ["192.168.100.1", "192.168.100.100"])
def test_send_sh_ip_int_br(device_example, ssh_connection, ipaddress):
    output = send_show_command(device_example, "sh ip int br")
    assert ipaddress in output
    correct_output = ssh_connection.send_command("sh ip int br")
    assert correct_output == output


def test_send_sh_cdp_neighbors(device_example, ssh_connection):
    """
    Проверяем что функция возвращает всех соседей
    parse_cdp_n  возвращает только соседей, без интерфейсов
    """
    output = send_show_command(device_example, "sh cdp neighbors")
    correct_output = ssh_connection.send_command("sh cdp neighbors")
    assert parse_cdp_n(correct_output) == parse_cdp_n(output)


def test_send_cfg(device_example):
    command = "logging 1.1.1.1"
    result = send_config_commands(device_example, command)
    assert command in result


def test_send_sh_devices(device_example, ssh_connection, tmpdir):
    filename = tmpdir.join("output_test.txt")
    send_show_to_devices([device_example], "sh ip int br", filename)
    file_content = filename.read()
    assert device_example["host"] in file_content
