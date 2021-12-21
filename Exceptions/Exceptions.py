#Exceptions

# print(a)             #NameError

s = 'Amin'
# print(s + 1)         #TypeError

# s.append('Golzari')  #AttributeError

lst = [1, 2, 3]
# print(lst[3])        #IndexError

# print(lst + 4)       #TypeError
# lst.add(5)           #AttributeError

d = {'a': 1, 'b': 2}
# print(d['f'])         #KeyError

# x = 8 / 0             #ZeroDivisionError

print('\n---------------------------------')

# print(k)   #NameError: name 'k' is not defined
try:
    print(k)
except NameError:
    print('Error')  #Error

print('Python')     #Python

print('\n---------------------------------')

try:
    print(k)
except NameError as ne:
    print(ne)  #name 'k' is not defined

print('\n---------------------------------')

s = 'Amin'

try:
    print(s + 4)
except TypeError as te:
    print(te)  #can only concatenate str (not "int") to str

print('\n---------------------------------')

try:
    x = 8 / 0
except ZeroDivisionError as ze:
    print(ze)  #division by zero
else:
    print(x)

#or

try:
    x = 8 / 2
except ZeroDivisionError as ze:
    print(ze)
else:
    print(x)  #4.0

print('\n---------------------------------')

def divide(x, y):
    try:
        r = x / y
    except ZeroDivisionError as ze:
        print(ze)
    else:
        print(r)
    finally:
        print('best wishes')

divide(2, 1)  #2.0 best wishes
divide(2, 0)  #division by zero best wishes

print('\n---------------------------------')

s = '23'
try:
    i = int(s)
except ValueError:
    i = -1

print(i)  #23

print('\n---------------------------------')

def f(n):
    try:
        if n == 13:
            raise ValueError('Unlucky Number')
        return 20 / n
    except (ZeroDivisionError, TypeError):
        return 'enter a new number!'

print(f(5))    #4.0

print(f(0))    #enter a new number!

print(f('a'))  #enter a new number!

# print(f(13))  #ValueError: Unlucky Number

print('\n----------------Nested try_except Blocks-----------------')

try:
    print(5 / 0)
    try:
        print(n)
    except NameError as ne:
        print(ne)
except ZeroDivisionError as ze:
    print(ze)     #division by zero

#or

try:
    print(5 / 2)   #2.5
    try:
        print(n)
    except NameError as ne:
        print(ne)   #name 'n' is not defined
except ZeroDivisionError as ze:
    print(ze)

print('\n---------------------------------')

try:
    n = int(input('enter: '))
    assert n % 2 == 0
except:
    print('Not Even')
else:
    print(n * 2)

#  دانشگاه شهید مدنی آذربایجان
#  برنامه نویسی مقدماتی با پایتون
#  امین گلزاری اسکوئی
# https://github.com/Amin-Golzari-Oskouei/Python-Programming-Course-Basic-2021
# https://drive.google.com/drive/folders/1ZsQjBJJ4UAAp9zrGxm3c4qrhnvGBUYHw




























