a = int(input("Enter the a value:"))
b = int(input("Enter the b value:"))
c = int(input("Enter the c value:"))
d = b**2 - 4*a*c
root1 = ((-b + (d**(0.5)))/2*a)
root2 = ((-b - (d**(0.5)))/2*a)
print(f"Roots are:{root1} and {root2}" )