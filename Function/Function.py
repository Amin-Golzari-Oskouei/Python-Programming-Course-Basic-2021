"""
function
"""

def Hello_1():
    print('Hello World!')

Hello_1()         #Hello World!

print('\n---------------------------------')

def Hello_2():
    return 'Hello World!'

R = Hello_2()
print(R)         #Hello World!

print('\n---------------------------------')

def Hello_3(p):
    print(p)

Hello_3('Hello World!')         #Hello World!

print('\n---------------------------------')

def Hello_4(p):
    return p

R = Hello_4('Hello World!')
print(R)         #Hello World!

print('\n---------------------------------')

def addtwo(a, b):
    return a + b

print(addtwo(1, 2))                  #3
print(addtwo('Hello ' ,'World!'))    #Hello World!

print('\n---------------------------------')

def f(a):
    a *= 2
    print(a)          #10
    return a + 1

b = 5
R = f(b)
print(R)             #11

print('\n---------------------------------')

def f(x, y):
    if x > y:
        return x
    return y

R = f(12, 5)
print(R)        #12

print('\n---------------------------------')

def g(x, y, z):
    return f(x, f(y, z))

R = g(12, 5, 1)
print(R)        #f(12, f(5,1)) = f(12, 5) = 12

print('\n---------------------------------')

PI = 3.14

def Masahat(r):
    return PI * r * r

def Mohit(r):
    return PI * r * 2

r = 3
print(Masahat(r))   #28.259999999999998
print(Mohit(r))     #18.84

print('\n---------------------------------')

x = 1

def f():
    x = 2
    print(x)   #2

f()
print(x)        #1

print('\n---------------------------------')

x = 1

def f():
    global x
    x = 2
    print(x)   #2

f()
print(x)        #2

print('\n---------------------------------')

x = 5
def func():
    global x
    print(x)   #5
    x = 8
    print(x)   #8

func()
print(x)       #8

print('\n---------------------------------')

def f(a, b):
    a -= 1
    b += 1
    return a, b

x = 3
y = 5
m, n = f(x, y)
print(m, n)   #2 6

print('\n---------------------------------')

def f(a):
    a[0] -= 1
    a[1] += 1

lst = [3, 5]
f(lst)
print(lst)   #[2, 6]


print('\n---------------------------------')

def f(d):
    d['a'] -= 1
    d['b'] += 1

my_dict = {'a': 3, 'b':5}
f(my_dict)
print(my_dict)    #{'a': 2, 'b': 6}

print('\n---------------------------------')

def f(a, b):
    print(a, b)

f(1, 2)            #1 2
f(a = 1, b = 2)    #1 2
f(1, b = 2)        #1 2
# f(2, a = 1)        #TypeError: f() got multiple values for argument 'a'

print('\n---------------------------------')

def f(a, b = 5, c = 7):
    print(a, b, c)

f(1)                    #1 5 7
f(1, 3)                 #1 3 7
f(1, 3 ,5)              #1 3 5
f(1, c = 9)             #1 5 9
f(c = 7, a = 5, b = 6)  #5 6 7
# f(1, b = 5, 6)          #SyntaxError: positional argument follows keyword argument

print('\n---------------------------------')

# keyword inly argument
def f(*, a = 3):
    print(a)

f()            #3
f(a = 5)       #5
# f(5)         #TypeError

print('\n---------------------------------')

# var arguments
def f(*t):
    s = 0
    for i in t:
        s += i
    print(s)

f(1, 2, 3)      #6
f(1, 3)         #4

print('\n---------------------------------')

def add(a, b, *more):
    r = a + b + sum(more)
    print(r)

add(1, 2, 3)        #6
add(1, 2)           #3
add(1, 2, 3, 4, 5)  #15

print('\n---------------------------------')

def f(a, b, *more):
    print(more)

f(1, 2, 3)        #(3,)
f(1, 2)           #()
f(1, 2, 3, 4, 5)  #(3, 4, 5)

print('\n---------------------------------')

def concat(*s, sep ='.'):
    return sep.join(s)

print(concat('ali', 'reza'))                #ali.reza
print(concat('ali', 'reza', sep='/'))       #ali/reza

print('\n---------------------------------')

def f(a, *, b = 2, c = 3):
    print(a, b, c)

f(1)                  #1 2 3
f(1, b = 8)           #1 8 3
# f(1, 3, c = 4)      #TypeError
# f(1, b = 3, 4)      #SyntaxError: positional argument follows keyword argument

print('\n---------------------------------')

def f(a, b, **c):
    print(a, b, c)

f(3, 4, x = 2, y = 5)      #3 4 {'x': 2, 'y': 5}

print('\n---------------------------------')

def f(a, b, *c, **d):
    print(a) #1
    print(b) #2
    print(c) #(3, 4, 5)
    print(d) #{'x': 6, 'y': 7}

f(1, 2, 3, 4, 5, x = 6, y = 7)

print('\n---------------------------------')

count_dict = {'L':0 , 'U':0}

def func_count(s):
    for ch in s:
        if ch.islower():
            count_dict['L'] += 1
        else:
            count_dict['U'] += 1

s = 'AmINGolzaRI'
func_count(s)
print(count_dict)    #{'L': 5, 'U': 6}

print('\n---------------------------------')

d = {}

def count_char(s):
    for ch in s:
        if ch in d.keys():
            d[ch] += 1
        else:
            d[ch] = 1


s = 'abcabhbh'
count_char(s)
print(d)      #{'a': 2, 'b': 3, 'c': 1, 'h': 2}

print('\n---------------------------------')

def count_word(s):
    d ={}
    words = s.split()
    for i in words:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    return d

s = 'python was created by Rossum'
print(count_word(s))             #{'python': 1, 'was': 1, 'created': 1, 'by': 1, 'Rossum': 1}

print('\n---------------------------------')

'''
switch(a){
   case 1:return 'one' ;break;
   case 2:return 'two' ;break;
   defualt :return 'nothing';
}
'''

def switch(a):
    d = {1 :'one', 2:'two'}
    return d.get(a, 'nothing')

print(switch(1))    #one
print(switch(2))    #two
print(switch(3))    #nothing

print('\n---------------------------------')

grade_student = [{'id': 123, 'M': 60, 'F':85},
                 {'id': 456, 'M': 70, 'F':50}]

def ave_grade(lst):
    for d in lst:
        n1 = d.pop('M')
        n2 = d.pop('F')
        d['Ave'] = (n1 + n2) /2
    return lst

print(ave_grade(grade_student))    #[{'id': 123, 'Ave': 72.5}, {'id': 456, 'Ave': 60.0}]

print('\n---------------------------------')

def reverse_string(s):
    r = ''.join(reversed(s))
    return r

print(reverse_string('abc'))      #cba
print(list(reversed('abc')))      #['c', 'b', 'a']

print('\n---------------------------------')

def palindrome(s):
    return s == s[::-1]

print(palindrome('radar'))      #True
print(palindrome('ali'))        #False

print('\n---------------------------------')

def remove_index(s, start, end):
    if len(s) > end:
        s = s[0: start] + s[end+1 ::]
    return s

s = 'python'
print(remove_index(s, 1, 3))   #pon

print('\n---------------------------------')

def remove_oddindex(s):
    r = ''
    for i in range(len(s)):
        if i % 2 == 0:
            r += s[i]
    return r

print(remove_oddindex('python'))   # pto

print('\n---------------------------------')

def unique_list(lst):
    r = []
    for i in lst:
        if i not in r:
            r.append(i)
    return r

a = [1, 2, 3, 1, 4, 2]
print(unique_list(a))    #[1, 2, 3, 4]

#or

def unique_list(lst):
    return list(set(lst))

a = [1, 2, 3, 1, 4, 2]
print(unique_list(a))    #[1, 2, 3, 4]

print('\n---------------------------------')

def f(n):
    r = [1]
    for i in range (2, n+1):
        if (n % i) == 0:
            r.append(i)
    return r

lst = f(10)
print(lst)          #[1, 2, 5, 10]

print('\n---------------------------------')

def f(s):
    w = ''
    lst = []
    for i in range(0, len(s)):
        if (s[i] != ' '):
            w += s[i]
        else:
            lst.append(w)
            w = ''

    m = lst[0]
    for j in range(0, len(lst)):
        if (len(lst[j]) > len(m)):
            m = lst[j]
    return m

s = 'deep learning with python is translated by Golzari'
print(f(s))      #translated

print('\n---------------------------------')

'''
1
1  1
1  2  1
1  3  3  1
1  4  6  4   1
'''

def pascal(n):
    t = [1]
    y = [0]
    for x in range(max(n, 0)):
        print(t)
        t = [i+j for i,j in zip(t+y, y+t)]

pascal(9)

# [1]
# [1, 1]
# [1, 2, 1]
# [1, 3, 3, 1]
# [1, 4, 6, 4, 1]
# [1, 5, 10, 10, 5, 1]
# [1, 6, 15, 20, 15, 6, 1]
# [1, 7, 21, 35, 35, 21, 7, 1]
# [1, 8, 28, 56, 70, 56, 28, 8, 1]

print('\n---------------------------------')

def f(s):
    my_set = set()
    w = s.split()
    for i in w:
        if i in my_set:
            return i
        else:
            my_set.add(i)
    return 'None'

s = 'sara amin ali amin reza ali'
print(f(s))    #amin

print('\n---------------------------------')

def prime(n):
    my_set = set()
    lst = []
    for i in range(2, n+1):
        if i in my_set:
            continue
        for j in range(i*2, n+1, i):
            my_set.add(j)
        lst.append(i)
    return lst

n = 10
print(prime(n))      #[2, 3, 5, 7]

print('\n---------------------------------')

def  magic(m):

    n = len(m[0])
    lst = []


    lst.extend([sum(i) for i in m])

    for col in range(n):
        lst.append(sum(row[col] for row in m))

    r1 = 0
    for i in range(0, n):
        r1 += m[i][i]
    lst.append(r1)

    r2 = 0
    for i in range(0, n):
        r2 += m[i][n-1-i]

    lst.append(r2)

    if len(set(lst)) > 1:
        return False
    return True

my_matrix = [[2, 7, 6],
             [9, 5, 1],
             [4, 3, 8]]

print(magic(my_matrix))   #true

print('\n---------------------------------')

print('--- PEP 484 -----')

def greeting(name):
    return 'Hello ' + name

print(greeting('farshid'))         # Hello farshid

def greeting(name: str) -> str:
    return 'Hello ' + name

print(greeting('farshid'))         # Hello farshid

print('\n---------------------------------')

def add(x:int, y:int) -> int:
    '''
     sum two number
    '''
    print(x+y)

add(2, 3)     #5

print(add.__annotations__)
# {'x': <class 'int'>, 'y': <class 'int'>, 'return': <class 'int'>}

print(add.__doc__)   # sum two number

#  دانشگاه شهید مدنی آذربایجان
#  برنامه نویسی مقدماتی با پایتون
#  امین گلزاری اسکوئی
# https://github.com/Amin-Golzari-Oskouei/Python-Programming-Course-Basic-2021
# https://drive.google.com/drive/folders/1ZsQjBJJ4UAAp9zrGxm3c4qrhnvGBUYHw











































































































































































































