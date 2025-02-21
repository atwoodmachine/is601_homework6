import sys
from calculator.commands import Command


class ExitCommand(Command):
    def execute(self):
        sys.exit("Exiting...")
    
    def description(self):
        return "Quit the calculator program"

    def usage(self):
        return "exit"