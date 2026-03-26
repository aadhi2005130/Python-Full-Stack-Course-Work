Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
s=set()
s={1458, 2344, 6688, 888,1323}
s
{6688, 1458, 888, 2344, 1323}
s.add(124)
s
{6688, 1458, 888, 2344, 1323, 124}
s.remove(124)
s
{6688, 1458, 888, 2344, 1323}
s.add(12.4)
s
{6688, 1458, 888, 2344, 1323, 12.4}
s.pop()
6688
s.discard(124)
s
{1458, 888, 2344, 1323, 12.4}
s.add(False)
s
{False, 1458, 888, 2344, 1323, 12.4}
s.update(123,56,68)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    s.update(123,56,68)
TypeError: 'int' object is not iterable
s.update(2i+3j)
SyntaxError: invalid decimal literal
s.update(2i+3)
SyntaxError: invalid decimal literal
s.update(2+3j)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    s.update(2+3j)
TypeError: 'complex' object is not iterable
s.add(2i+3j)
SyntaxError: invalid decimal literal
s.add(2+3j)
s
{False, 1458, 888, 2344, 1323, 12.4, (2+3j)}
s.update{(123,56,68)}
SyntaxError: invalid syntax
s.update({123,56,68})
s
{False, 68, 2344, 1323, 12.4, (2+3j), 1458, 888, 56, 123}
s.pop()
68
>>> s.pop()
2344
>>> for i in s:
...     print(i)
... 
...     
False
1323
12.4
(2+3j)
1458
888
56
123
>>> a = {1,2,3,4}
>>> b = {3,4,1,6}
>>> a|b
{1, 2, 3, 4, 6}
>>> a-b
{2}
>>> #{9}{8}{5}{3}{6}{9,7}{7,5}
>>> {9}>a
False
>>> {9}<a
False
>>> a.disjoint(b)
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    a.disjoint(b)
AttributeError: 'set' object has no attribute 'disjoint'. Did you mean: 'isdisjoint'?
>>> a.isisdisjoint(b)
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    a.isisdisjoint(b)
AttributeError: 'set' object has no attribute 'isisdisjoint'. Did you mean: 'isdisjoint'?
>>> a.isdisjoint(b)
False
>>> a.union(b)
{1, 2, 3, 4, 6}
>>> {0}.isjoint(a)
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    {0}.isjoint(a)
AttributeError: 'set' object has no attribute 'isjoint'. Did you mean: 'isdisjoint'?
>>> {0}.isdisjoint(a)
True
>>> min(a)
1
>>> sorted(a)
[1, 2, 3, 4]
>>> max(a)
4
>>> len(a)
4
