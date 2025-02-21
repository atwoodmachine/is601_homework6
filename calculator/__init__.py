import pkgutil
import importlib
from calculator.commands import CommandHandler
from calculator.commands import Command


class Calculator:
    def __init__(self):
        self.command_handler = CommandHandler()

    def load_plugins(self):
        plugins_package = 'calculator.plugins'

        for i, plugin_name, is_pkg in pkgutil.iter_modules([plugins_package.replace('.', '/')]):
            if is_pkg:
                plugin_module = importlib.import_module(f'{plugins_package}.{plugin_name}')
                for item_name in dir(plugin_module):
                    item = getattr(plugin_module, item_name)
                    try:
                        if issubclass(item, (Command)):
                            self.command_handler.register_command(plugin_name, item())
                    except TypeError:
                        continue

    def start(self):
        Calculator.load_plugins(self)
        print("Calculator initialized\n")
        print("Type 'exit' to quit\n")

        while True:
            self.command_handler.handle_user_input(input("> ").strip())