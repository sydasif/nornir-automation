from nornir import InitNornir
from nornir_napalm.plugins.tasks import napalm_ping
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yaml")


def ping_dest_ip(task):
    task.run(task=napalm_ping, dest="10.0.0.6")


results = nr.run(task=ping_dest_ip)
print_result(results)
