Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> d = {}
>>> type(d)
<class 'dict'>
>>> d = dict()
>>> d
{}
>>> s=set()
>>> data = {'name': 'adi', 'age': 21, 'course': 'PFS','skills':['python','java']}
>>> data
{'name': 'adi', 'age': 21, 'course': 'PFS', 'skills': ['python', 'java']}
>>> data['name']
'adi'
>>> data['skils']
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    data['skils']
KeyError: 'skils'
>>> data['skills']
['python', 'java']
>>> d[1]
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    d[1]
KeyError: 1
>>> d[1.1] = 'float'
>>> d
{1.1: 'float'}
>>> data
{'name': 'adi', 'age': 21, 'course': 'PFS', 'skills': ['python', 'java']}
>>> d['dff'] = 'string'
>>> d
{1.1: 'float', 'dff': 'string'}
>>> d[True] = 'boolean'
>>> d
{1.1: 'float', 'dff': 'string', True: 'boolean'}
>>> id(d)
2163340239616
>>> d['age'] = 21
>>> d
{1.1: 'float', 'dff': 'string', True: 'boolean', 'age': 21}
>>> d.items()
dict_items([(1.1, 'float'), ('dff', 'string'), (True, 'boolean'), ('age', 21)])
>>> d.values()
dict_values(['float', 'string', 'boolean', 21])
>>> d.keys()
dict_keys([1.1, 'dff', True, 'age'])
>>> d['name'] = adi
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    d['name'] = adi
NameError: name 'adi' is not defined
>>> d['name'] = 'adi'
>>> d
{1.1: 'float', 'dff': 'string', True: 'boolean', 'age': 21, 'name': 'adi'}
data
{'name': 'adi', 'age': 21, 'course': 'PFS', 'skills': ['python', 'java']}
sorted(data)
['age', 'course', 'name', 'skills']
max(data)
'skills'
min(data)
'age'
data['kl'] = ''vl'
SyntaxError: unterminated string literal (detected at line 1)
data['kl'] = 'vl'
data
{'name': 'adi', 'age': 21, 'course': 'PFS', 'skills': ['python', 'java'], 'kl': 'vl'}
data.update['adress':'miyapur','college':'mr']
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    data.update['adress':'miyapur','college':'mr']
TypeError: 'builtin_function_or_method' object is not subscriptable
data.update(['adress':'miyapur','college':'mr'])
SyntaxError: invalid syntax
data.update({'adress':'miyapur','college':'mr'})
data
{'name': 'adi', 'age': 21, 'course': 'PFS', 'skills': ['python', 'java'], 'kl': 'vl', 'adress': 'miyapur', 'college': 'mr'}
