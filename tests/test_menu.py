from decimal import Decimal
import pytest
from calculator import Calculator
from calculator.plugins.add import AddCommand
from calculator.plugins.subtract import SubtractCommand
from calculator.plugins.divide import DivideCommand
from calculator.plugins.multiply import MultiplyCommand

def test_add_description(capfd):
    command = AddCommand()
    assert command.description() == "Add two operands: a + b", "Add description should output 'Add two operands: a + b'"

def test_add_usage(capfd):
    command = AddCommand()
    assert command.usage() == "add <operand_a> <operand_b>", "Add usage should output 'add <operand_a> <operand_b>'"

def test_subtract_description(capfd):
    command = SubtractCommand()
    assert command.description() == "Subtract two operands: a - b", "Add description should output 'Subtract two operands: a - b'"

def test_subtract_usage(capfd):
    command = SubtractCommand()
    assert command.usage() == "subtract <operand_a> <operand_b>", "Subtract usage should output 'subtract <operand_a> <operand_b>'"

def test_multiply_description(capfd):
    command = MultiplyCommand()
    assert command.description() == "Multiply two operands: a * b", "Multiply description should output 'Multiply two operands: a + b'"

def test_multiply_usage(capfd):
    command = MultiplyCommand()
    assert command.usage() == "multiply <operand_a> <operand_b>", "Multiply usage should output 'multiply <operand_a> <operand_b>'"

def test_divide_description(capfd):
    command = DivideCommand()
    assert command.description() == "Divide two operands: a / b, where b is not equal to zero", "Divide description should output 'Divide two operands: a / b, where b is not equal to zero'"

def test_divide_usage(capfd):
    command = DivideCommand()
    assert command.usage() == "divide <operand_a> <operand_b>", "Divide usage should output 'divide <operand_a> <operand_b>'"
