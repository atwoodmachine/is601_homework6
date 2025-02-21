import pkgutil
import importlib
import inspect
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

                    constructor_params = inspect.signature(item.__init__).parameters

                    try:
                        if issubclass(item, (Command)):
                            if 'command_handler' in constructor_params:
                                self.command_handler.register_command(plugin_name, item(self.command_handler))
                            else:
                                self.command_handler.register_command(plugin_name, item())
                    except TypeError:
                        continue

    def start(self):
        Calculator.load_plugins(self)
        print("Calculator initialized\nType 'exit' to quit. Type 'menu' to see available commands.\n")

        while True:
            self.command_handler.handle_user_input(input("> ").strip())