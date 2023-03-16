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


def multiplication(numbers):
    value = 1
    for i in numbers:
        value *= i
    return value


def division(numbers):
    value = numbers.pop(0)
    for i in numbers:
        try:
            value /= i
        except:
            return "\nYou cannot deivide numbers by 0!\n"
    return value


def exponential(x, y):
    return x ** y
