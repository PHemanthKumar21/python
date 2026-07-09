Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#arthematic
a=2
b=4
print(a+b)
6
print(a-b)
-2
print(a*b)
8
print(a//b)
0
print(a/b)
0.5
print(a%b)
2
#assignment operators
a=4
b=6
print(a+=b)
SyntaxError: invalid syntax
b+=a
b+=4
b
14
b-=7
b-=4
b//=4
b
0
b+=8
b
8
b-=15
b
-7
b+=20
b
13
b*=2
b
26
b//=2
b
13
b/=4
b
3.25
b%=4
b
3.25
#comaparision operators
a=2
b=6
a<b
True
b<a
False
a<=b
True
b<=a
False
a!=b
True
a==b
False
a=2
b=4
a==b
False
#logical operators
a=6
b=8
a<b and b>a
True
a<=b and b>=a
True
a!=b and a==b
False
a!=b or a==b
True
not true
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    not true
NameError: name 'true' is not defined. Did you mean: 'True'?
>>> not True
False
>>> not False
True
>>> #identify operators
>>> a=7
>>> type(a) is complex
False
>>> type(a) is int
True
>>> type(a) is float
False
>>> type(a) is str
False
>>> type(a) is bool
False
>>> b="hemanth"
>>> type(b) is str
True
>>> type(b) is int
False
>>> type(b) is float
False
>>> type(b) is complex
False
>>> type(b) is bool
False
>>> type(b) is not bool
True
>>> c=3.4
>>> type(c)=int
SyntaxError: cannot assign to function call here. Maybe you meant '==' instead of '='?
>>> type(c) is int
False
>>> type(c) is float
True
>>> type(c) is not float
False
>>> #Membership operators
a=2,4,5,7,8,9,2
7 in a
True
10 in a
False
4 in a
True
4 not in a
False
b="python,"java","c",
SyntaxError: unterminated string literal (detected at line 1)
b="python","java","c"
java not in b
Traceback (most recent call last):
  File "<pyshell#83>", line 1, in <module>
    java not in b
NameError: name 'java' is not defined
"java" not in b
False
#bitwise operator
a=4
b=6
a&b
4
bin(a)
'0b100'
bin(b)
'0b110'
a=5
b=2
a&b
0
bin(a)
'0b101'
bin(b)
'0b10'
a=4
b=6
a|b
6
#not -(x+1)
a=4
-(a+10)
-14
a
4
b=6
-(x+1)
Traceback (most recent call last):
  File "<pyshell#105>", line 1, in <module>
    -(x+1)
NameError: name 'x' is not defined
b=8
-(b+1)
-9
c=-8
-(c+1)
7
~c
7
#^
a=3
b=2
a^b
1
a=5
a<<2
20
b=6
b>>3
0
c=8
c<<4
128
