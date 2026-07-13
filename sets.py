Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #set
>>> a={3,7.3,"hemanth",3+6j,True,False}
>>> print(a)
{False, True, 3, (3+6j), 7.3, 'hemanth'}
>>> type(a)
<class 'set'>
>>> b={35,8,9,24,90}
>>> print(b)
{35, 8, 9, 90, 24}
>>> #issubset
>>> a={2,3,6,8,9,10}
>>> b={8,9,10}
>>> a.issubset(b)
False
>>> b.issubset(a)
True
>>> #add
>>> a={4,5,6,7,8}
>>> a.add(22)
>>> a
{4, 5, 6, 7, 8, 22}
>>> #issuperset
>>> a={4,5,6,7,8,9}
>>> b={7,8,9}
>>> a.issuperset(b)
True
>>> b.issuperset(a)
False
#union
a={3,4,5,6,7}
b={1,2,3,4,5,6,7}
a.union(b)
{1, 2, 3, 4, 5, 6, 7}
#intersection
a={3,4,5,6,7}
b={1,2,3,7,8,9}
a.intersection(b)
{3, 7}
b.intersection(a)
{3, 7}
#difference
a={7,8,9,10,11,12,13}
b={8,9,10,11,12,13,14,15}
a.difference(b)
{7}
b.difference(a)
{14, 15}
#update
a={2,3,4,5,6}
b={1,3,4,8,9,10}
a.update(b)
a
{1, 2, 3, 4, 5, 6, 8, 9, 10}
b
{1, 3, 4, 8, 9, 10}
b.update(a)
b
{1, 2, 3, 4, 5, 6, 8, 9, 10}
#symmetric difference
a={2,3,4,5,7,8}
b={1,4,6,8,9,10,11}
a.symmetric_difference(b)
{1, 2, 3, 5, 6, 7, 9, 10, 11}
b.symmetric_difference(a)
{1, 2, 3, 5, 6, 7, 9, 10, 11}
#difference_update
a={4,5,6,7,8,9}
b={2,4,5,6,8,9,10}
a.difference_update(b)
a
{7}
b.difference_update(a)
b
{2, 4, 5, 6, 8, 9, 10}
#intersection_update
a={3,4,5,6,7,8,9}
b={5,6,7,8,3,9,10}
a.intersection_update(b)
a
{3, 5, 6, 7, 8, 9}
b.intersection_update(a)
b
{3, 5, 6, 7, 8, 9}
#symmetric_difference_update
a={11,12,13,14,15,16}
b={24,13,14,16,20,18}
a.symmetric_difference_update(b)
a
{11, 12, 15, 18, 20, 24}
#pop and remove
a={3,4,5,6,7,8}
a.pop()
3
a
{4, 5, 6, 7, 8}
a.pop(1)
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    a.pop(1)
TypeError: set.pop() takes no arguments (1 given)
a.pop(5)
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    a.pop(5)
TypeError: set.pop() takes no arguments (1 given)
a.remove(5)
a
{4, 6, 7, 8}
#copy
a={4, 6, 7, 8}
a.copy()
{8, 4, 6, 7}
#discard
a={20,30,40,50}
a.discard(30)
a
{40, 50, 20}
#clear
a=
KeyboardInterrupt
KeyboardInterrupt
a={10,20,40,33}
a.clear()
a
set()
a={2,3,5,7,8}
b={6,4,1,10,2}
a.disjoint(b)
Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    a.disjoint(b)
AttributeError: 'set' object has no attribute 'disjoint'. Did you mean: 'isdisjoint'?
a.isdisjoint(b)
False
c={6,4,1,10,2}
d={11,30,3,5}
c.isdisjoint(d)
True
