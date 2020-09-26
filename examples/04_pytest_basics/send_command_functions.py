from netmiko import ConnectHandler
import re


def send_show_command(device, command):
    with ConnectHandler(**device) as ssh:
        ssh.enable()
        result = ssh.send_command(command)
    return result


def send_config_commands(device, config_commands):
    with ConnectHandler(**device) as ssh:
        ssh.enable()
        result = ssh.send_config_set(config_commands)
    return result


def parse_cdp_n(output):
    regex = r"^(\S+) +\S+ +\S+ +\d+"
    return re.findall(regex, output, re.MULTILINE)



if __name__ == "__main__":
    r1 = {
        "device_type": "cisco_ios",
        "host": "192.168.100.100",
        "username": "cisco",
        "password": "cisco",
        "secret": "cisco",
    }
    result = send_show_command(r1, "sh cdp neighbors")
    print(parse_cdp_n(result))

