from pathlib import Path

from nornir import InitNornir
from nornir_netmiko.tasks import netmiko_send_command
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yaml")

commands_file = Path(__file__).parent / "show_commands.txt"
commands = [
    line.strip() for line in commands_file.read_text().splitlines() if line.strip()
]


def send_show_cmds_from_file(task):
    for command in commands:
        task.run(task=netmiko_send_command, command_string=command)


results = nr.run(task=send_show_cmds_from_file)
print_result(results)
