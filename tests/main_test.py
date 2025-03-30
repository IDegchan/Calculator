from src.main import button_press # type: ignore

def test_buttons():
    assert button_press("10", "AC") == "0"
    assert button_press("7", "R")   == "-7"
    assert button_press("10", "B")  == "1"
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