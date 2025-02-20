from decimal import Decimal
from calculator.commands import Command

class DivideCommand(Command):
    def execute(self, a: Decimal, b: Decimal):
        try:
            print(f"Result: {a / b}")
        except ZeroDivisionError:
            print("Math error: division by zero")