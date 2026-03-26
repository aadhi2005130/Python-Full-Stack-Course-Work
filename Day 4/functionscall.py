def add(a, b):
    return (a + b)

def multiply(a, b):
    return (a * b)

def divide(a, b):
    return (a / b)

def subtract(a, b):
    return (a - b)

def modulus(a, b):
    return (a % b)

exp = input("Enter expression: ")

if '+' in exp:
    a, b = exp.split('+')
    print(add(int(a), int(b)))

elif '*' in exp:
    a, b = exp.split('*')
    print(multiply(int(a), int(b)))

elif '/' in exp:
    a, b = exp.split('/')
    print(divide(int(a), int(b)))

elif '-' in exp:
    a, b = exp.split('-')
    print(subtract(int(a), int(b)))

elif '%' in exp:
    a, b = exp.split('%')
    print(modulus(int(a), int(b)))