from src.main import button_press # type: ignore
import math

def test_buttons():
    assert button_press("10", "AC") == "0"
    assert button_press("7", "R")   == "-7"
    assert button_press("10", "B")  == "1"
    assert button_press("5", "0")   == "50"
    assert button_press("0", "1")   == "1"
    assert button_press("3", "2")   == "32"
    assert button_press("5", "3")   == "53"
    assert button_press("8", "4")   == "84"
    assert button_press("4", "5")   == "45"
    assert button_press("0", "6")   == "6"
    assert button_press("99", "7")  == "997"
    assert button_press("1", "8")   == "18"
    assert button_press("645", "9") == "6459"
    assert button_press("90", ".")  == "90."
    assert button_press("0", "+")   == "0+"
    assert button_press("0", "-")   == "0-"
    assert button_press("0", "*")   == "0*"
    assert button_press("0", "/")   == "0/"
    assert button_press("0", "^")   == "0^"
    assert button_press("3", "=")   == "3"

def test_errors():
    assert button_press("5+", "=") == "Помилка :("
    assert button_press("7-", "=") == "Помилка :("
    assert button_press("1*", "=") == "Помилка :("
    assert button_press("8/", "=") == "Помилка :("
    assert button_press("9^", "=") == "Помилка :("
    assert button_press("0/", "=") == "Помилка :("
    assert button_press("0^", "=") == "Помилка :("
    assert button_press("^0", "=") == "Помилка :("

def test_advanced():
    assert button_press("π", "=") == "3.141592653589793"
    assert button_press("e", "=") == "2.718281828459045"
    assert button_press("tan(7)", "=") == f"{math.tan(7)}"
    assert button_press("cos(2)", "=") == f"{math.cos(2)}"
    assert button_press("sin(6)", "=") == f"{math.sin(6)}"
    assert button_press("factorial(5)", "=") == f"{math.factorial(5)}"
