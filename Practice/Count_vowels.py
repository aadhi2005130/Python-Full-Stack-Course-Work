#count the number of vowels in a string
name = input("Enter a string to count the vowels in: ")
name2 = name.lower()
a = name2.count("a")
e = name2.count("e")
i = name2.count("i")
o = name2.count("o")
u = name2.count("u")
print(f"The number of vowels in the string is: {a+e+i+o+u}")