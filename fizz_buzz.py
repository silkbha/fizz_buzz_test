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
        return n + 2


