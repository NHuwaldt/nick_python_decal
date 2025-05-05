def add(a, b):
    return a + b
#returns the addition of two numbers
def subtract(a, b):
    return a - b
#returns the difference between two numbers, sign sensitive
def multiply(a, b):
    return a * b
#returns the product of two numbers
def divide(a, b):
    if b == 0:
        return "Invalid input, division by zero"
    else:
        return a / b
#returns the quotient of a divided by b without division by zero
