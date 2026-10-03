from nornir import InitNornir
from nornir_scrapli.tasks import send_command
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file='config.yaml')

commands = ["show ip int brief | include up", "show run | include version"]


def send_show_cmds(task):
    for command in commands:
        task.run(task=send_command, command=command)


result = nr.run(task=send_show_cmds)
print_result(result)
