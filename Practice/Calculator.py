n1 = int(input("Enter the first number"))
n2 = int(input("Enter the second number"))
operation = input("Enter the operation you want to perform")
if operation == "+":
    print(n1+n2)
elif operation == "-":
    print(n1-n2)
elif operation == "*":
    print(n1*n2)
elif operation == "/":
    print(n1/n2)
else:
    print("Invalid operation")