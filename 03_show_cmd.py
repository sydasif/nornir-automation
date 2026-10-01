from nornir import InitNornir
from nornir_scrapli.tasks import send_command
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file='config.yaml')


def send_show_cmd(task):
    task.run(task=send_command, command="show run | include ntp")


result = nr.run(task=send_show_cmd)
print_result(result)
