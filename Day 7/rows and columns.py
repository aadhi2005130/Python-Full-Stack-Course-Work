'''
n = int(input("Enter the size: "))
for i in range(n):
    for j in range(n):
        print("*",end='&')
    print()
'''
'''
n = int(input("Enter the size: "))
for row in range(n):
    for col in range(n):
        if (row + col) % 2 == 0:
            print('0', end='')
        else:
            print('1', end='')
    print()
'''
'''
n = int(input("Enter the size: "))
for row in range(n):
    for col in range(row+1):
        print('*', end='')
    print()
'''
'''
n=int(input("Enter the size: "))
for row in range(n):
    for col in range(n-row):
        print('*', end='')
    print()
'''
'''
n = int(input("Enter the size: "))
for row in range(n):
    for col in range(n):
        if row == 0 or row == n-1 or col == 0 or col == n-1:
            print('*', end='')
        else:
            print(' ', end='')
    print()
'''
'''
n = int(input("Enter the size: "))
for row in range(n):
        for spc in range(n-row):
            print(' ', end='')
        for col in range(row+1):
            print('*', end='')
        print()
'''
#print in all in the form of z stars shape
'''
n = int(input("Enter the size: "))
for row in range(n):
    for col in range(n):
        if row == 0 or row == n-1 or row + col == n-1:
            print('*', end='')
        else:
            print(' ', end='')
    print()
'''
#print in the form of x stars shape
'''
n = int(input("Enter the size: "))
for row in range(n):
    for col in range(n):
        if row == col or row + col == n-1:
            print('*', end='')
        else:
            print(' ', end='')
    print()
'''
#print all the letters in my name in the form of stars and input should be given by the user
name = input("Enter your name: ")
n = int(input("Enter the size: "))
for row in range(n):
    for col in range(n):
        if row == 0 or row == n-1 or col == 0 or col == n-1:
            print('*', end='')
        else:
            print(' ', end='')
    print()