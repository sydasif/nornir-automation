from nornir import InitNornir
from nornir_scrapli.tasks import send_commands
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file='config.yaml')

commands = ["show ip int brief", "show version", "show run"]


def send_show_cmds(task):
    task.run(task=send_commands, commands=commands)


results = nr.run(task=send_show_cmds)
print_result(results)
