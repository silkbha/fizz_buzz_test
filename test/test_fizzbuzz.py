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
