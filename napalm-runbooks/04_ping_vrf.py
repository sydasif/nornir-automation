from nornir import InitNornir
from nornir_napalm.plugins.tasks import napalm_ping
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yaml")


def ping_vrf_ip(task):
    task.run(task=napalm_ping, dest="192.168.121.106", vrf="clab-mgmt")


results = nr.run(task=ping_vrf_ip)
print_result(results)
