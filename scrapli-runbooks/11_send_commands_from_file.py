from pathlib import Path

from nornir import InitNornir
from nornir_scrapli.tasks import send_commands_from_file
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file='config.yaml')

commands_file = Path(__file__).parent / "show_commands.txt"


def send_show_cmds_from_file(task):
    task.run(task=send_commands_from_file, file=str(commands_file))


results = nr.run(task=send_show_cmds_from_file)
print_result(results)
