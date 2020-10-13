from concurrent.futures import ThreadPoolExecutor
from pprint import pprint
from datetime import datetime
import time
from itertools import repeat
import logging
import click

import yaml
from netmiko import ConnectHandler, NetMikoAuthenticationException

logging.getLogger("netmiko").setLevel(logging.INFO)
logging.getLogger("paramiko").setLevel(logging.WARNING)

logging.basicConfig(
    format="%(threadName)s %(name)s - %(levelname)s: %(message)s",
    level=logging.DEBUG
)


def send_show(device_dict, command):
    ip = device_dict["host"]
    logging.info(f"===>  Connection: {ip}")

    with ConnectHandler(**device_dict) as ssh:
        ssh.enable()
        result = ssh.send_command(command)
        logging.debug(f"<===  Received:   {ip}")
    return result


def send_command_to_devices(devices, command):
    logging.debug(click.style("START", fg="green"))
    data = {}
    with ThreadPoolExecutor(max_workers=2) as executor:
        result = executor.map(send_show, devices, repeat(command))
        for device, output in zip(devices, result):
            data[device["host"]] = output
    return data


if __name__ == "__main__":
    with open("devices.yaml") as f:
        devices = yaml.safe_load(f)
    send_command_to_devices(devices, "sh ip int br")
