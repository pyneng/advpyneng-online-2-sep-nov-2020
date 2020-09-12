from itertools import repeat
from concurrent.futures import ThreadPoolExecutor
from netmiko import ConnectHandler
import yaml
from typing import Dict, Union, List


DictStrAny = Dict[str, Union[str, int, bool]]

def send_show_command(device: DictStrAny, command: str) -> str:
    with ConnectHandler(**device) as ssh:
        test = "test"
        ssh.enable()
        result: str = ssh.send_command(command)
        prompt = ssh.find_prompt()
    return f"{prompt}{command}\n{result}\n"


def send_show_command_to_devices(
    devices: List[DictStrAny], command: str, filename: str, limit: int = 3
) -> None:
    with ThreadPoolExecutor(max_workers=limit) as executor:
        results = executor.map(send_show_command, devices, repeat(command))
        with open(filename, "w") as f:
            for output in results:
                f.write(output)


if __name__ == "__main__":
    command = "sh ip int br"
    with open("devices.yaml") as f:
        devices: List[DictStrAny] = yaml.safe_load(f)
    send_show_command_to_devices(devices, command, "result.txt")
    reveal_type(devices)
