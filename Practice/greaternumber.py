numbers = input("")
a,b,c = numbers.split(',')
a,b,c = int(a),int(b),int(c)
if a > b and a > c:
    print(f"The greatest number is: {a}")
elif b > a and b > c:
    print(f"The greatest number is: {b}")
else:
    print(f"The greatest number is: {c}")