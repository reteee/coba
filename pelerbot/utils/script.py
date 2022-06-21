from pelerbot import COMMAND_HANDLER
from .misc import module_help


def format_module_help(module_name: str):
    commands = modules_help[module_name]

    help_text = f"<b>Help for |{module_name}|\n\nUsage:</b>\n"

    for command, desc in commands.items():
        cmd = command.split(maxsplit=1)
        args = " <code>" + cmd[1] + "</code>" if len(cmd) > 1 else ""
        help_text += f"<code>{COMMAND_HANDLER}{cmd[0]}</code>{args} — <i>{desc}</i>\n"

    return help_text


def format_small_module_help(module_name: str):
    commands = modules_help[module_name]

    help_text = f"<b>Help for |{module_name}|\n\nCommands list:\n"
    for command, desc in commands.items():
        cmd = command.split(maxsplit=1)
        args = " <code>" + cmd[1] + "</code>" if len(cmd) > 1 else ""
        help_text += f"<code>{COMMAND_HANDLER}{cmd[0]}</code>{args}\n"
    help_text += f"\nGet full usage: <code>{COMMAND_HANDLER}help {module_name}</code></b>"

    return help_text
