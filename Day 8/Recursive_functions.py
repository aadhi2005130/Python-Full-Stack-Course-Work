#recursive fuction
''''
def display(n):
    if n>0:
        print(n)
        display(n-1)
display(10)
'''
'''
def display(n):
    if n>10:
        return
    print(n)
    display(n+1)
display(1)

#display the string "Python Programming" in output using recursion
def display(s,i):
    if i >= len(s):
        return
    display(s,i+1)
    print(s[i])

display("Python Programming", 0)

def display(s,i):
    if i == len(s):
        return
    display(s,i+1)
    print(s[:i+1])

display("Python Programming", 0)

#abc,5
#abc
#abcabcabc
#abcabcabcabcabc using recursion
def display(i,s):
    if i<=0:
        return
    display(i-1,s)
    print(i*s)
display(5,"abc")
'''
#abcdefg,3
#abc
#bcd
#cde
#def
#egh
'''
def display(s,i,n):
    if i>len(s)-n:
        return
    print(s[i:i+n])
    display(s,i+1,n)
display("abcdefghijkl",0,5)
'''
'''
#[1,2,3,4,5] = ? #find the sum of the list using recursion
def display(l,i,sum):
    if i == len(l):
        return sum
    return display(l,i+1,sum+l[i])
print(display([1,2,3,4,5],0,0))
'''
'''
#['python', 'java', 'html', 'css', 'javascript','flask']] = ? #give output like this using recursion
def display(l,i,sum):
    if i == len(l):
        return sum
    return display(l,i+1,sum+l[i])
print(display(['python', 'java', 'html', 'css', 'javascript','flask'],0,''))
'''
#int,float,string,list,tuple,dictionary,set = ? #find the count of each data type in the list using recursion
def display(n):
    n+=(8,9)
    print("Inside:",n)
n=(1,2,3,4)
display(n)
print("Outside:",n)