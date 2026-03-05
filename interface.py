from calculator import Calculator

calc = Calculator()

def calculate(operation, a, b=None):

    if operation == "+":
        return calc.add(a, b)

    if operation == "-":
        return calc.subtract(a, b)

    if operation == "*":
        return calc.multiply(a, b)

    if operation == "/":
        return calc.divide(a, b)

    if operation == "C":
        return calc.clear()

    raise ValueError("Invalid operation")
