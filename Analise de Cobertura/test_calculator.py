import calculator
import pytest
from io import StringIO
import sys

# Helper function to simulate input and capture output
def run_calculator_input(inputs):
    sys.stdin = StringIO("\n".join(inputs))
    sys.stdout = StringIO()  # Capture output
    calculator.calculator()
    sys.stdin = sys.__stdin__  # Reset stdin
    return sys.stdout.getvalue()  # Return the captured output

def test_addition():
    result = run_calculator_input(['1', '10', '5', '7'])  # 10 + 5 = 15
    assert "10.0 + 5.0 = 15.0" in result

def test_subtraction():
    result = run_calculator_input(['2', '10', '5', '7'])  # 10 - 5 = 5
    assert "10.0 - 5.0 = 5.0" in result

def test_multiplication():
    result = run_calculator_input(['3', '10', '5', '7'])  # 10 * 5 = 50
    assert "10.0 * 5.0 = 50.0" in result

def test_division():
    result = run_calculator_input(['4', '10', '2', '7'])  # 10 / 2 = 5
    assert "10.0 / 2.0 = 5.0" in result

def test_division_by_zero():
    result = run_calculator_input(['4', '10', '0', '7'])  # Division by zero
    assert "Erro: Divisão por zero não é permitida." in result

def test_power():
    result = run_calculator_input(['5', '2', '3', '7'])  # 2 ^ 3 = 8
    assert "2.0 elevado a 3.0 = 8.0" in result

def test_square_root():
    result = run_calculator_input(['6', '9', '7'])  # sqrt(9) = 3
    assert "Raiz quadrada de 9.0 = 3.0" in result

def test_exit():
    result = run_calculator_input(['7'])  # Exit
    assert "Saindo da calculadora." in result
