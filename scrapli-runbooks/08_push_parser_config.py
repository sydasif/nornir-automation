from nornir import InitNornir
from nornir_scrapli.tasks import send_configs_from_file
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file='config.yaml')


def send_config_file(task):
    task.run(task=send_configs_from_file, file="parser_config.cfg")


result = nr.run(task=send_config_file)
print_result(result)
