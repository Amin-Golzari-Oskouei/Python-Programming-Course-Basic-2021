"""
Operators :
    Arithmetic : +,-,*,/,%,**,//
    Assignment : =,+=,-=,*= ,/= ,%= ,//= ,**=
    Comparison : ==,!=,>,<,>=,<=
    Logical    : and, or, not
    Membership : in , not in
    Bitwise    :  &, |, ^, ~, <<, >>
"""

print('Arithmetic Operators')

# Add
print(1 + 5)   #6

# Sub
print(1 - 5)   #-4

# mul
print(6 * 5)   #30

# Float Division
print(6 / 5)   #1.2

# Integer Division
print(6 // 5)   #1

# mod
print(6 % 3)   #0

# Pow
print(6 ** 2)   #36
print(0 ** 0)   #1
print(6 ** 0)   #1

print('Operator Precedence')
print(8 - 2 * 3)     #2
print(8 + 2 / 3)     #8.6
print(16 / 2 ** 3)   #2.0
print(16 // 2 ** 3)  #2
print(2**2**3)       #256
print((2**2)**3)     #64

print('Augmented Assignment Operator')
x = 4
x += 1      # x = x + 1
print(x)    #5

x = 4
x -= 1      # x = x - 1
print(x)    #3

x = 4
x /= 3      # x = x / 3
print(x)    #1.33

x = 4
x //= 3      # x = x // 3
print(x)     #1

x = 4
x %= 3      # x = x % 3
print(x)    #1

x = 4
x **= 3      # x = x ** 3
print(x)     #64

print('Comparison Operators')

print(2 == 2)   #True
print(2 != 2)   #False
print(2 < 2)    #False
print(2 <= 2)   #True

print('Logical Operators')

print(1 < 3 and 4 > 5)   #False
print(1 < 3 or 4 > 5)    #True
print(not 1 < 3)         #False

print(1 >= 2 and (5/0) > 2)    #False
# print((5 / 0) > 2 and 1 >= 2)  #ZeroDivisionError: division by zero

print(2 >= 1 or (5/0) > 2)    #True
# print((5 / 0) > 2 or 1 >= 2)  #ZeroDivisionError: division by zero

print('Membership Operators')

x = [1, 2, 3, 4, 5, 7]
print(3 in x)   #True
print(6 in x)   #False

print(3 not in x)   #False
print(6 not in x)   #True

print('Bitwise Operators')

a = 13
print(bin(a))  #0b1101

b = 14
print(bin(b))  #0b1110

# or
c = a | b
print(c)       #15
print(bin(c))  #0b1111

#and
c = a & b
print(c)       #12
print(bin(c))  #0b1100

#xor
c = a ^ b
print(c)       #3
print(bin(c))  #0b0011

#shift
a = 13
print(a << 1)   #26   a * (2 ** 1)
print(a << 2)   #52   a * (2 ** 2)

print(a >> 1)   #6   a // (2 ** 1)
print(a >> 2)   #3   a // (2 ** 2)

a = 13
print(~a)   # -(a + 1)

a = 0
print(~a)   # -(a + 1)

a = -10
print(~a)   # -(a + 1)

print('--- Operations on string ---')

s1 = 'Amin'
s2 = ' Golzari Oskouei'

s3 = s1 + s2  #Amin Golzari Oskouei
print(s3)

s1 = '1'
s2 = '2'

s3 = s1 + s2  #12
print(s3)

s = 'Python'
print(3 * (s + ' '))    # Python Python Python


#Every object in python is stored somewhere in memory.
#We can use id() to get that memory address.

s1 = 'Ali'
s2 = 'Ali'

print(id(s1) == id(s2))    #True

s1 += ' Ali'
print(s1)
print(id(s1) == id(s2))    #False

print(id(s1))
print(id(s2))

print(abs(-4))       #4
print(pow(2, 3))     #8
print(round(2.6))    #3
print(round(2.3))    #2
print(round(2.5))    #2

print(abs.__doc__)   #Return the absolute value of the argument.

import math
print(math.sqrt(4))          #2.0
print(math.pow(2,3))         #8.0
print(math.trunc(2.3))       #2
print(math.trunc(2.8))       #2
print(math.floor(2.8))       #2
print(math.ceil(2.8))        #3
print(math.factorial(3))     #6
print(math.log(8,2))         #3.0
print(math.log2(8))          #3.0
print(math.log10(100))       #2.0
print(math.pi)

print(dir(math))             #['__doc__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'comb', 'copysign', 'cos', 'cosh', 'degrees', 'dist', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'isqrt', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'perm', 'pi', 'pow', 'prod', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'tau', 'trunc']

import random
print(random.randint(1 , 5))
print(random.choice([1, 5, 6, 7, 8]))
a = [1, 2, 3, 4]
random.shuffle(a)
print(a)

import datetime
now = datetime.datetime.now()
print(now)
print(now.year)
print(now.month)
print(now.day)

import sys
print(sys.version)    #3.8.8 (default, Apr 13 2021, 15:08:03) [MSC v.1916 64 bit (AMD64)]
print(sys.platform)   #win32

import platform
print(platform.release())    #10

import os
print(os.getcwd())  #E:\teaching\python\Basic\Pycharm\Operators

#  دانشگاه شهید مدنی آذربایجان
#  برنامه نویسی مقدماتی با پایتون
#  امین گلزاری اسکوئی
# https://github.com/Amin-Golzari-Oskouei/Python-Programming-Course-Basic-2021
# https://drive.google.com/drive/folders/1ZsQjBJJ4UAAp9zrGxm3c4qrhnvGBUYHw




























































