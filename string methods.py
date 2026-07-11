Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#len()
a="hemanth"
print(a)
hemanth
a="hemanth"
len(a)
7
a="codegnan"
len(a)
8
b="vijayawada "
len(b)
11
c=""
len(c)
0
d=" "
len(d)
1
e="i am in  vijayawada"
len(e)
19
#count
a="hemanth kumar"
a.count(n)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    a.count(n)
NameError: name 'n' is not defined
a.count("n")
1
a.count("h")
2
a.count("t")
1
a="vijayawada city"
a.count("a")
4
a,count("i")
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    a,count("i")
NameError: name 'count' is not defined. Did you mean: 'round'?
>>> a.count("i")
2
>>> a.count(" ")
1
>>> a.count("")
16
>>> #find a string
>>> a="python"
>>> a.find("o")
4
>>> a.find("n")
5
>>> b="codegnan"
>>> b.find("a")
6
>>> b.find("e")
3
>>> #escape sequences
>>> a="name:hemanth\nmailid:poolahemanthnaidu@gmail.com\tbranch:cse\ncollege:kare\tstream:aiml"
>>> print("a")
a
>>> print(a)
name:hemanth
mailid:poolahemanthnaidu@gmail.com	branch:cse
college:kare	stream:aiml
>>> #replace
>>> a="wait until you succeed"
>>> a.replace("wait","work")
'work until you succeed'
>>> b="python java"
b.replace("p","c")
'cython java'
c="wait until you succeed"
c="wait until you succeed"
c="wait wait until you succeed"
c.replace("wait","work")
'work work until you succeed'
c.replace("wait","work",1)
'work wait until you succeed'
#lower()
a="code"
a.lower()
'code'
a="CODE"
a.lower()
'code'
a="code"
a.upper()
'CODE'
c="python"
c.capitalize()
'Python'
c="python course"
c.title()
'Python Course'
c="code"
c.isupper()
False
c.islower()
True
c.isdigit()
False
c.isalpha()
True
b="python course"
b.isalpha()
False
b.isdigit()
False
c="pythoncourse"
c.isdigit
<built-in method isdigit of str object at 0x0000020F3FC0E5F0>
c.isupper()
False
d=1234
d.isdigit()
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    d.isdigit()
AttributeError: 'int' object has no attribute 'isdigit'
a="1234'
SyntaxError: unterminated string literal (detected at line 1)
a="1234"
a.isdigit()
True
a="1,2,3,4,"
a.isdigit()
False
b="hemanth123"
a.isalnum()
False
b.isalnum()
True
c="hemanth.1234"
c.isalnum()
False
a="data science"
a.startswith("d")
True
a.endswith("a")
False
a.endswith("e")
True
True
True
#strip
#lstrip(),rstrip()
a="hemanthkumar  "
a.strip()
'hemanthkumar'
c="    hemanth  "
c.rstrip()
'    hemanth'
c.lstrip()
'hemanth  '
b="python java c c++"
b="python java c c++"
b.split()
['python', 'java', 'c', 'c++']
x="i love vijayawada"
x.strip()
'i love vijayawada'
x.split()
['i', 'love', 'vijayawada']
#join
a="html","css","js"
"".join(a)
'htmlcssjs'
" ".join(a)
'html css js'
c="python"
"d".join(c)
'pdydtdhdodn'
#concatenation
a="code"
b="gnan"
print(a+b)
codegnan
fname="hemanth"
lname="kumar"
print(fname+lname)
hemanthkumar
print(fname+" "+lname)
hemanth kumar
print(fname.title()+" "+lname.title())
Hemanth Kumar
print(fname+" "+lname).title())
SyntaxError: unmatched ')'
print((fname+" "+lname).title())
Hemanth Kumar
#formatting
a=6
b=5
print(a+b)
11
print("sum is",a+b)
sum is 11
b="vijayawada"
print("city is",b)
city is vijayawada
#format
a="motu"
b="pathlu"
print("hello {} {}".format(a,b))
hello motu pathlu
print("hello {}{}".format(a,b))
hello motupathlu
print("hello {}\nhello {}".format(a,b))
hello motu
hello pathlu
#fstring
a"sitha"
SyntaxError: invalid syntax
a="sitha"
b="ram"
print(f"hello {a}{b}")
hello sitharam
print(f"hello{a} hello {b}")
hellositha hello ram
print(f"hello {a}n\ hello {b}")
hello sithan\ hello ram
print(f"hello {a}\n hello {b}")
hello sitha
 hello ram
