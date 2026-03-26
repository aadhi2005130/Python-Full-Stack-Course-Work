s = input("Enter a string to check if it's a palindrome: ")
if s == s[::-1]:
    print("it is a palindrome")
else:
    print("it is not a palindrome")