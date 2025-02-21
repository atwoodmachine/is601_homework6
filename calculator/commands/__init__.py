from abc import ABC, abstractmethod
from decimal import Decimal, InvalidOperation

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

class CommandHandler:
    def __init__(self):
        self.commands = {}

    def register_command(self, command_name: str, command: Command):
        self.commands[command_name] = command

    def execute_command(self, command_name: str, *args):
        try:
            self.commands[command_name].execute(*args)
        except KeyError:
            print(f"Command not recognized: {command_name}")
    
    def handle_user_input(self, input: str):
        user_input = input.split()
        command_name = user_input[0]
        try:
            args = list(map(Decimal, user_input[1:]))
            self.execute_command(command_name, *args)
        except InvalidOperation:
            print("Error: argument entered was not a valid number")
        except Exception as e:
            print(f"Error: {e}")