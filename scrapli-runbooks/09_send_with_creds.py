import getpass

from nornir import InitNornir
from nornir_scrapli.tasks import send_command
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file='config.yaml')

iol_password = getpass.getpass("Enter IOL Password: ")
iosv_password = getpass.getpass("Enter iOSV Password: ")

nr.inventory.groups["iol"].password = iol_password
nr.inventory.groups["iosv"].password = iosv_password


def send_show_cmd(task):
    task.run(task=send_command, command="show version | include uptime")


results = nr.run(task=send_show_cmd)
print_result(results)
