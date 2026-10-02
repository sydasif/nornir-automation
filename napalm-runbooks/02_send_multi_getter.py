from nornir import InitNornir
from nornir_napalm.plugins.tasks import napalm_get
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yaml")


def get_device_info(task):
    task.run(task=napalm_get, getters=["get_users", "get_interfaces_ip"])


results = nr.run(task=get_device_info)
print_result(results)
