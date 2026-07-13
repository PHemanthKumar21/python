Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #tuple
>>> a=(2,5.3,"python",4+6j,True,False)
>>> print(a)
(2, 5.3, 'python', (4+6j), True, False)
>>> type(a)
<class 'tuple'>
>>> a.index(True)
4
>>> len(a)
6
>>> a.count(True)
1
>>> a.index(5.3)
1
