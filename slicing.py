Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#slicing
a="codegnan"
a[0:5]
'codeg'
a[0:4]
'code'
a[4:8]
'gnan'
a[:4]
'code'
a[4:]
'gnan'
a="work until you succeed"
a[0:5]
'work '
a[6:11]
'ntil '
a[6:10]
'ntil'
>>> a[5:10]
'until'
>>> a[15:21]
'succee'
>>> a[15:22]
'succeed'
>>> a[11:14]
'you'
>>> a="time is very precious"
>>> a[13:21]
'precious'
>>> b[8:12]
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    b[8:12]
NameError: name 'b' is not defined
>>> a[8:12]
'very'
>>> a[0:4]
'time'
>>> #-positive
>>> b="simple is better than complex"
>>> b="simple is better than complex"
>>> b[-7:-1]
'comple'
>>> b[-7:]
'complex'
>>> b[-19:-13]
'better'
>>> b[-29:-23]
'simple'
>>> c="codegnan it solutions"
>>> c[-9:-1]
'solution'
>>> c[-21:-13]
'codegnan'
