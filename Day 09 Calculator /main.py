def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

def mod(a, b):
    return a % b


num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
sign = input("Please select sign (+, -, *, /, %): ")

result = 0

match sign:
    case '+':
        result = add(num1, num2)

    case '-':
        result = sub(num1, num2)

    case '*':
        result = mul(num1, num2)

    case '/':
        result = div(num1, num2)

    case '%':
        result = mod(num1, num2)

    case _:
        print("❌ Invalid operator")
        result = None


if result is not None:
    print("Result:", result)