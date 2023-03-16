def addition(numbers):
    sum = 0
    for i in numbers:
        sum += i
    return sum


def subtraction(numbers):
    value = numbers.pop(0)
    for i in numbers:
        value -= i
    return value


def multiplication(x, y):
    return x / y


def division(x, y):
    return x / y


def exponential(x, y):
    return x ** y
