from nornir import InitNornir
from nornir_netmiko.tasks import netmiko_send_command
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yaml")

command_list = ["show version | include Version", "show version | include uptime"]


def send_show_command(task):
    for command in command_list:
        task.run(task=netmiko_send_command, command_string=command)


results = nr.run(task=send_show_command)
print_result(results)
