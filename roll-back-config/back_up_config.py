from nornir import InitNornir
from nornir_scrapli.tasks import send_interactive
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yaml")


def commit_flash(task):
    # on ios use 'flash:', on iol use 'unix:'
    commands = [("copy run unix:base", "Destination filename"), ("\n", f"{task.host}#")]
    task.run(task=send_interactive, interact_events=commands)


results = nr.run(task=commit_flash)
print_result(results)
