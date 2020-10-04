from netmiko import ConnectHandler


r1_dict = {
    'device_type': 'cisco_ios',
    'host': '192.168.100.1',
    'username': 'cisco',
    'password': 'cisco',
    'secret': 'cisco'
}
r2_dict = {
    'device_type': 'cisco_ios',
    'host': '192.168.100.2',
    'username': 'cisco',
    'password': 'cisco',
    'secret': 'cisco'
}


def connect_ssh(device):
    print(f"Подключаюсь к {device['host']}")
    ssh = ConnectHandler(**device)
    ssh.enable()
    def send_show_command(command):
        print(f"Отправляю команду {command} на {device['host']}")
        output = ssh.send_command(command)
        return output
    return send_show_command
