import pytest
def fizz_buzz(n):
    if n <= 0:
        raise ValueError("Input must be a positive integer")
    elif n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    else:
        return n

def test_fizz_buzz():
    assert fizz_buzz(3) == "Fizz"

def test_fizz_buzz1():
    assert fizz_buzz(5) == "Buzz"

def test_fizz_buzz2():
    assert fizz_buzz(15) == "FizzBuzz"

def test_fizz_buzz3():
    assert fizz_buzz(7) == 7

def test_fizz_buzz4():
    with pytest.raises(ValueError):
        fizz_buzz(0)

def test_fizz_buzz5():
    with pytest.raises(ValueError):
        fizz_buzz(-1)

def test_fizz_buzz6():
    assert fizz_buzz(1) == 1

def test_fizz_buzz7():
    assert fizz_buzz(2) == 2

def test_fizz_buzz8():
    assert fizz_buzz(4) == 4
