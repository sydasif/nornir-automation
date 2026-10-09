from nornir import InitNornir
from nornir_netmiko.tasks import netmiko_multiline
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yaml")

commands = ["show clock", "show version | include Version"]


def send_show_commands(task):
    task.run(task=netmiko_multiline, commands=commands)


results = nr.run(task=send_show_commands)
print_result(results)
