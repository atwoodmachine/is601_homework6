from decimal import Decimal
from calculator.commands import Command

class MultiplyCommand(Command):
    def execute(self, a: Decimal, b: Decimal):
        print(f"Result: {a * b}")