'''
a=[]
for i in range(1,100):
    if i%2==0:
        a.append(i)
print(a)
'''
'''
v=[]
for i in range(1,100,3):
    v.append(i)
print(v)
'''
'''
#using list comprehension
a=[i for i in range(1,100) if i%2==0]
print(a)
v=[i for i in range(1,100,3)]
print(v)
'''
'''
s = "Python is a great language"
vowels = 'aeiouAEIOU'
l=['*' if i in vowels else i for i in s]
print(l)
'''
'''
l = [7, 8, 9, 10, 11, 12, 13, 14, 15]
l = [0 if i%2==0 else i for i in l]
print(l)
'''
l = [7, 8, 9, 10, 11, 12, 13, 14, 15]
rl = [i**l.count(i) for i in l]
print(rl)
