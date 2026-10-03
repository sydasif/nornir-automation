from nornir import InitNornir
from nornir_scrapli.tasks import send_command
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file='config.yaml')


def rollback_config(task):
    # on ios use 'flash:', on iol use 'unix:'
    groups = {device.name for device in task.host.groups}
    if "iol" in groups:
        command = "configure replace unix:base force"
    else:
        command = "configure replace flash:base force"
    task.run(task=send_command, command=command)


result = nr.run(task=rollback_config)
print_result(result)
