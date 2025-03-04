from abc import ABC, abstractmethod
from decimal import Decimal, InvalidOperation
import logging
import logging.config

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass
    @abstractmethod
    def description(self):
        pass
    @abstractmethod
    def usage(self):
        pass

class CommandHandler:
    def __init__(self):
        self.commands = {}

    def register_command(self, command_name: str, command: Command):
        self.commands[command_name] = command
        logging.info(f"Command '{command_name}' registered.")

    def execute_command(self, command_name: str, *args):
        try:
            self.commands[command_name].execute(*args)
            logging.info(f"Command '{command_name}' executed.")
        except KeyError:
            logging.error(f"Command not recognized: {command_name}")
            print(f"Command not recognized: {command_name}")
    
    def handle_user_input(self, input: str):
        user_input = input.split()
        command_name = user_input[0]
        try:
            args = list(map(Decimal, user_input[1:]))
            self.execute_command(command_name, *args)
        except InvalidOperation:
            logging.error(f"Error: command '{command_name}' with invalid argument")
            print("Error: argument entered was not a valid number")
        except Exception as e:
            logging.error(f"Exception: {e}")
            print(f"Error: {e}")
