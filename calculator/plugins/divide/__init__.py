from decimal import Decimal
from calculator.commands import Command

class DivideCommand(Command):
    def execute(self, a: Decimal, b: Decimal):
        try:
            print(f"Result: {a / b}")
        except ZeroDivisionError:
            print("Math error: division by zero")

    def description(self):
        return "Divide two operands: a / b, where b is not equal to zero"
    
    def usage(self):
        return "divide <operand_a> <operand_b>"