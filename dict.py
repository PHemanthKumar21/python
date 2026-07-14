Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
 #dict()
a={"name":"hemanth","year":2026,"month":7}
a
{'name': 'hemanth', 'year': 2026, 'month': 7}
type(a)
<class 'dict'>
a.keys()
dict_keys(['name', 'year', 'month'])
a.values()
dict_values(['hemanth', 2026, 7])
>>> a.items()
dict_items([('name', 'hemanth'), ('year', 2026), ('month', 7)])
>>> a={"year":2026,"month":"july","date":14}
>>> a.update("
...          
SyntaxError: unterminated string literal (detected at line 1)
>>> a.update({"time":2})
...          
>>> a
...          
{'year': 2026, 'month': 'july', 'date': 14, 'time': 2}
>>> a.update(["time":2},{"day":"tue"})
...          
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
>>> a.update({"time":2,"day":"tue"})
...          
>>> a
...          
{'year': 2026, 'month': 'july', 'date': 14, 'time': 2, 'day': 'tue'}
>>> a={"name":"hemanth","city":"vja"}
...          
>>> a.setdefault("mail","hemanth@gmail.com")
...          
'hemanth@gmail.com'
>>> a
...          
{'name': 'hemanth', 'city': 'vja', 'mail': 'hemanth@gmail.com'}
>>> a={"state":"ap","country":"india"}
         
a.pop("country")
         
'india'
a
         
{'state': 'ap'}
a.popitem()
         
('state', 'ap')
a
         
{}
#copy
         
a={"colour":"blue","food":"biryani"}
         
a.copy()
         
{'colour': 'blue', 'food': 'biryani'}
b=a.copy()
         
b
         
{'colour': 'blue', 'food': 'biryani'}
len(a)
         
2
#there is no count and index in dict
         
a={"name":"hemanth","city":"vja","name":"hemanth"}
         
print(a)
         
{'name': 'hemanth', 'city': 'vja'}
a={"name":"hemanth","city":"vja","name":"ajay"}
         
a
         
{'name': 'ajay', 'city': 'vja'}
a={"name1":"hemanth","city":"vja","name2":"hemanth"}
         
a
         
{'name1': 'hemanth', 'city': 'vja', 'name2': 'hemanth'}
a.count()
         
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    a.count()
AttributeError: 'dict' object has no attribute 'count'
a.count()
         
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    a.count()
AttributeError: 'dict' object has no attribute 'count'
a.clear()
         
a
         
{}
b={}
         
b.update({"name":"hemanth"}
b
         
SyntaxError: '(' was never closed
b.update{"name":"hemanth"}
         
SyntaxError: invalid syntax
b.update({"name":"hemanth"})
         
b
         
{'name': 'hemanth'}
#single key no.of values
         
a={"idnos":[10,20,30],"names":["hemanth","sai","pawan"],"marks":[60,70,80]}
         
print(a)
         
{'idnos': [10, 20, 30], 'names': ['hemanth', 'sai', 'pawan'], 'marks': [60, 70, 80]}
a.keys()
         
dict_keys(['idnos', 'names', 'marks'])
a.values()
         
dict_values([[10, 20, 30], ['hemanth', 'sai', 'pawan'], [60, 70, 80]])
a.items()
         
dict_items([('idnos', [10, 20, 30]), ('names', ['hemanth', 'sai', 'pawan']), ('marks', [60, 70, 80])])
a=[9,1,5,2,8,4,6,7,0]
         
#[7,6,4,3,0,9,8,5,2,1]
         
a=[9,1,5,2,8,4,6,3,7,0]
         
a.sort()
         
a
         
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
