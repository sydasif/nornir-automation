from nornir import InitNornir
from nornir_netmiko.tasks import netmiko_send_config
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yaml")


def send_config_command(task):
    task.run(
        task=netmiko_send_config,
        config_commands=["router eigrp 12", "network 1.1.1.1", "network 2.2.2.2"],
    )


results = nr.run(task=send_config_command)
print_result(results)
