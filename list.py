Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#list
a=[2,3.5,"python",6+7j,True,False]
print(a)
[2, 3.5, 'python', (6+7j), True, False]
type(a)
<class 'list'>
b=8.9
type(b)
<class 'float'>
c=[6.5]
type(c)
<class 'list'>
#append
a=["python","httml","css"]
a.append("java")
a
['python', 'httml', 'css', 'java']
a.append("c","c++")
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    a.append("c","c++")
TypeError: list.append() takes exactly one argument (2 given)
a.append(["c","c++"])
a
['python', 'httml', 'css', 'java', ['c', 'c++']]
#extend
b=["vja","hyd","vizag"]
b.extend("chennai")
b
['vja', 'hyd', 'vizag', 'c', 'h', 'e', 'n', 'n', 'a', 'i']
b.extend(["chennai"])
b
['vja', 'hyd', 'vizag', 'c', 'h', 'e', 'n', 'n', 'a', 'i', 'chennai']
#insert
c=["python","data science","aiml"]
c.insert(1,"machine learning")
c
['python', 'machine learning', 'data science', 'aiml']
x=["java","c","c++"]
x.insert(2,"python")
x
['java', 'c', 'python', 'c++']
#index,copy
a=["apples","banana","grapes"]
a.index("grapes")
2
a.copy()
['apples', 'banana', 'grapes']
b=a.copy()
b
['apples', 'banana', 'grapes']
a.count("apples")
1
len(a)
3
d="apples"
len(d)
6
e=["apples"]
len(e)
1
#sort
a=["kiwi","dragon","berry","mango"]
a.sort()
a
['berry', 'dragon', 'kiwi', 'mango']
b=[7,3,4,2,9,6,11]
b.sort()
b
[2, 3, 4, 6, 7, 9, 11]
#reverse
a=["ds","ai","ml"]
a.reverse()
a
['ml', 'ai', 'ds']
b=[5,2,7,8,12]
a.reverse()
a
['ds', 'ai', 'ml']
b
[5, 2, 7, 8, 12]
>>> #pop
>>> a=["white","black","red","green"]
>>> a.pop()
'green'
>>> a
['white', 'black', 'red']
>>> a.pop(2)
'red'
>>> a
['white', 'black']
>>> b=["red","blue","yellow","grey"]
>>> b.pop("red")
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    b.pop("red")
TypeError: 'str' object cannot be interpreted as an integer
>>> b.remove("red")
>>> b
['blue', 'yellow', 'grey']
>>> #clear
>>> a=["python","httml","java"]
>>> a.clear()
>>> a
[]
>>> a.append(["c+"])
>>> a
[['c+']]
