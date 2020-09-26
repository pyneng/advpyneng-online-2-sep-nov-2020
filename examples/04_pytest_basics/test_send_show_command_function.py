from send_command_functions import send_show_command, send_config_commands, parse_cdp_n
from netmiko import ConnectHandler


def test_send_sh_ip_int_br(device_example, ssh_connection):
    output = send_show_command(device_example, "sh ip int br")
    assert device_example["host"] in output
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


def test_send_cfg(device_example, device_connection):
    command = "logging 1.1.1.1"
    result = send_config_commands(device_example, command)
    assert command in result
