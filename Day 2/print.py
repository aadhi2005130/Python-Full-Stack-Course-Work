a = 10
b = 22.5
c = "string"
d = False
e = 8*9
print(a,b,c,d,e)
print("a=",a,"b=",b,'c=',c,'d=',d,'e=',e)
print("a=",a,"b=",b,'c=',c,sep='',end=' ')
print("a=",a,"b=",b,'c=',c,sep='\n')
print("a=",a,"b=",b,'c=',c,sep='\n',end='\n\n')
print("a=",a,"b=",b,'c=',c,sep='$$$$$$',end='--------')
print(f"a= {a} b= {b} c= {c}")
print("a = %d b= %f c= %s"%(a,b,c))
print("a = {} b= {} c= {} d= {} e= {}".format(a,b,c,d,e))