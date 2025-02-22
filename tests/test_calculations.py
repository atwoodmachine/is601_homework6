# pylint: disable=invalid-name
'''Test set up for use with faker generated data'''
from decimal import Decimal
import pytest


def test_calculation_operation(a, b, command, expected, capfd):
    '''Tests calculation result'''
    command.execute(a, b)
    out, err = capfd.readouterr()
    assert out == expected
