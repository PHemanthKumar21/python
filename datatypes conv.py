Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#datatype conversions
int(18)
18
int(7.3)
7
int("hi")
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    int("hi")
ValueError: invalid literal for int() with base 10: 'hi'
int(9+5j)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    int(9+5j)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
int(True)
1
int(False)
0
#float
float(7)
7.0
float("hemanth")
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    float("hemanth")
ValueError: could not convert string to float: 'hemanth'
float(6+8j)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    float(6+8j)
TypeError: float() argument must be a string or a real number, not 'complex'
float(True)
1.0
float(False)
0.0
#string
str(24)
'24'
>>> str(9.3)
'9.3'
>>> str("hemanth")
'hemanth'
>>> str(5+4j)
'(5+4j)'
>>> str(True)
'True'
>>> str(False)
'False'
>>> #complex
>>> complex(45)
(45+0j)
>>> complex(5.0)
(5+0j)
>>> complex("hemanth")
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    complex("hemanth")
ValueError: complex() arg is a malformed string
>>> complex(6+2j)
(6+2j)
>>> complex(True)
(1+0j)
>>> complex(False)
0j
>>> #bool
>>> bool(16)
True
>>> bool(3.8)
True
>>> bool("hemanth")
True
>>> bool(8+5j)
True
>>> bool(True)
True
>>> bool(False)
False
