import pytest
from calculator import Calculator

def test_exit_command(capfd, monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 'exit')
    calc = Calculator()
    with pytest.raises(SystemExit) as e:
        calc.start()
    assert e.type == SystemExit

def test_unknown_command(capfd, monkeypatch):
    inputs = iter(['missing', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    calc = Calculator()
    with pytest.raises(SystemExit) as e:
        calc.start()
    output = capfd.readouterr()
    assert "Command not recognized: missing" in output.out