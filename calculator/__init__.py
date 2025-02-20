from calculator.commands import CommandHandler
from calculator.commands.add import AddCommand
from calculator.commands.subtract import SubtractCommand
from calculator.commands.multiply import MultiplyCommand
from calculator.commands.divide import DivideCommand
from calculator.commands.exit import ExitCommand

class Calculator:
    def __init__(self):
        self.command_handler = CommandHandler()

    def start(self):
        self.command_handler.register_command("add", AddCommand)
        self.command_handler.register_command("subtract", SubtractCommand)
        self.command_handler.register_command("multiply", MultiplyCommand)
        self.command_handler.register_command("divide", DivideCommand)
        self.command_handler.register_command("exit", ExitCommand)

        print("Calculator initialized\n")
        print("Type 'exit' to quit\n")

        while True:
            self.command_handler.handle_user_input(input("> ").strip())