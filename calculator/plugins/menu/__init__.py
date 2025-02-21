from calculator.commands import Command

class MenuCommand(Command):
    def __init__(self, command_handler):
        self.command_handler = command_handler
    
    def execute(self):
        all_commands = self.command_handler.commands
        for command_name, command_func in all_commands.items():
            print(f"Command: {command_name}")