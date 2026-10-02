from nornir import InitNornir
from nornir_scrapli.tasks import send_config
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file='config.yaml')


def send_config_cmd(task):
    task.run(task=send_config, config="ntp server 55.66.77.88")


result = nr.run(task=send_config_cmd)
print_result(result)
