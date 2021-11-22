"""
    list
    'index' ,'count','insert','remove','pop','reverse'
    , 'sort' ,'extend', 'append','clear','copy',

"""

a = [5, 7, 12]
print(type(a))      #<class 'list'>
print(len(a))       #3

print('\n-----------------------------------')

print(a.index(7))    #1
print(a[1])          #7
a[1] = 8
print(a)             #[5, 8, 12]

print('\n-----------------------------------')

s = 'sara'
print(s[1])
# s[1] = 'b'            #TypeError: 'str' object does not support item assignment

print('\n-----------------------------------')

a = [1, 2]
b = [2, 1]
print(a==b)     #False (list is ordered)

print('\n-----------------------------------')

friend = ['ali', 'sara', 'taha']
for f in friend:
    print(f, end =' ')     #ali sara taha

# or

friend = ['ali', 'sara', 'taha']
for f in range(3):
    print(friend[f], end =' ')     #ali sara taha

print('\n-----------------------------------')

L = [3, 6, True, False, 'ali', 2.7, [2, 5]]

print('\n-----------------------------------')

a = [7, 5, 30, 45, 74, 56, 8]
print(a[1:4])    #[5, 30, 45]
print(a[:4])     #[7, 5, 30, 45]
print(a[4:])     #[74, 56, 8]
print(a[3:0])    #[]
print(a[::-1])   #[8, 56, 74, 45, 30, 5, 7]
print(a[0:7:2])  #[7, 30, 74, 8]
print(a[6:0:-2]) #[8, 74, 30]

print('\n-----------------------------------')

a = [7, 5, 30, 45, 74, 56, 8]

a[3:5] = [4, 5]
print(a)         #[7, 5, 30, 4, 5, 56, 8]

print('\n-----------------------------------')

a = [1, 2]
b = a * 2
print(b)   #[1, 2, 1, 2]

print('\n-----------------------------------')

a = [1, 2]
b = ['a', 'b', 'c']
c = a + b
print(c)    #[1, 2, 'a', 'b', 'c']

print('\n-----------------------------------')

a = [7, 5, 30, 4, 5, 56, 8]

print(14 in a)         #False
print(14 not in a)     #True

print('\n-----------------------------------')

a = [3, [4, 1], 4, 15]
print(a[1])      #[4, 1]
print(a[1][0])   #4
print(len(a))    #4

print('\n-----------------------------------')

a = [7, 5, 30, 4, 5, 56, 8]
m = -1
for i in a:
    if i > m:
        m = i

print(m)     #56

print('\n-----------------------------------')

a = [7, 5, 30, 4, 5, 56, 8]
print(max(a))      #56
print(min(a))      #4
print(sum(a))      #115

print('\n-----------------------------------')

a = [7, 5, 30, 4, 5, 56, 8]
s = 0
for i in a:
    s += i

print(s)       #115

print('\n-----------------------------------')

a = [7, 7, 30, 5, 5, 56, 7]
print(a.count(7))   #3

print('\n-----------------------------------')

a = [7, 7, 30, 5, 5, 56, 7]
a.insert(2, 13)
print(a)        #[7, 7, 13, 30, 5, 5, 56, 7]

print('\n-----------------------------------')

a = [7, 7, 30, 5, 5, 56, 7]
x = a.pop()
print(a)        # [7, 7, 30, 5, 5, 56]
print(x)        # 7

print('\n-----------------------------------')

a = [7, 7, 30, 5, 5, 56, 7]
x = a.pop(2)
print(a)        # [7, 7, 5, 5, 56, 7]
print(x)        # 30

print('\n-----------------------------------')

a = [3, 5, 7]
del a[1]
print(a)  #[3, 7]

print('\n-----------------------------------')

a = [3, 5, 7]
del a
# print(a)  #NameError: name 'a' is not defined

a = [3, 5, 7]
del a[0:2]
print(a)  #[7]

print('\n-----------------------------------')

a = [3, 5, 7]
a.reverse()
print(a)    #[7, 5, 3]

print('\n-----------------------------------')

a = [3, 5, 7]
a.sort()
print(a)    #[3, 5, 7]

print('\n-----------------------------------')

x = [1, 2, 3]
y = [4, 5]
x.extend(y)
print(x)           #[1, 2, 3, 4, 5]
print(len(x))      #5
print((len(y)))    #2

print('\n-----------------------------------')

x = [1, 2, 3]
y = [4, 5]
y.extend(x)
print(y)           #[4, 5, 1, 2, 3]
print(len(x))      #3
print((len(y)))    #5

print('\n-----------------------------------')

x = [1, 2, 3]
y = [4, 5]
y.append(x)
print(y)           #[4, 5, [1, 2, 3]]
print(len(x))      #3
print((len(y)))    #5

print('\n-----------------------------------')

a = [1, 2, 3]
a.append(4)
print(a)           #[1, 2, 3, 4]

print('\n-----------------------------------')

a = [1, 2, 3]
a.clear()
print(a)                #[]
print(len(a))           #0

print('\n-----------------------------------')

a = [1, 2, 3]
b = a.copy()
print(b)                #[1, 2, 3]

print('\n-----------------------------------')

a = []
for i in range(4):
    a.append(i)

print(a)              #[0, 1, 2, 3]

#or

a = [i for i in range(4)]
print(a)              #[0, 1, 2, 3]

print('\n-----------------------------------')

a = [0, 1, 2, 3]
a = [i*2 for i in range(4)]
print(a)              #[0, 2, 4, 6]

print('\n-----------------------------------')

a = [0, 1, 2, 3]
a = [i**2 for i in range(4)]
print(a)              #[0, 1, 4, 9]

print('\n-----------------------------------')

a = [0, 1, 2, 3]
a = [i*i for i in range(4)]
print(a)              #[0, 1, 4, 9]

print('\n-----------------------------------')

a = [1, -1, 2, -3, -8]
b = [abs(i) for i in a]
print(b)              #[1, 1, 2, 3, 8]

print('\n-----------------------------------')

import math

a = [round(math.pi, i) for i in range(5)]
print(a)              #[3.0, 3.1, 3.14, 3.142, 3.1416]

print('\n-----------------------------------')

a = ['$ali', 'sara$']
b = [i.strip('$') for i in a]
print(b)           #['ali', 'sara']

print('\n-----------------------------------')

a = [8, 10, 11, 5, 4, 56]
b = [i for i in a if i < 10]
print(b)           #[8, 5, 4]

print('\n-----------------------------------')

a = [1, 2]
b = [1, 4, 5]
c = []
for i in a:
    for j in b:
        if i != j:
            c.append([i,j])
print(c)             #[[1, 4], [1, 5], [2, 1], [2, 4], [2, 5]]

print('\n-----------------------------------')

a = [2.6, float('NaN'), 4.8, 6.9, float('NaN')]
b = []
import math
for i in a:
    if not math.isnan(i):
        b.append(i)
print(b)           #[2.6, 4.8, 6.9]

print('\n-----------------Matrix------------------')
m = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(len(m))         #3
print(m[0])           #[1, 2, 3]
print(m[0][2])        #3

print('\n-----------------------------------')

for i in m:
    print(i)

# [1, 2, 3]
# [4, 5, 6]
# [7, 8, 9]

print('\n-----------------------------------')

for i in m:
    print(i[0], end =' ')      #1 4 7

print('\n-----------------------------------')

for i in range(0,3):
    print(m[i][i], end =' ')      #1 5 9

print('\n-----------------------------------')

for i in range(0, 3):
    print(m[i][2-i], end=' ')  # 3 5 7

print('\n-----------------------------------')

a = []
a.extend([sum(i) for i in m])
print(a)             #[6, 15, 24]

print('\n-----------------------------------')

b = []
for col in range(3):
    b.append(sum(i[col] for i in m))
print(b)             #[12, 15, 18]

print('\n-----------------------------------')

x = 2
y = x
y += 1
print(x)      #2
print(y)      #3

print('\n-----------------------------------')

x = []
y = x
y.append(5)
print(x)      #[5]
print(y)      #[5]

print('\n-----------------------------------')


#  دانشگاه شهید مدنی آذربایجان
#  برنامه نویسی مقدماتی با پایتون
#  امین گلزاری اسکوئی
# https://github.com/Amin-Golzari-Oskouei/Python-Programming-Course-Basic-2021
# https://drive.google.com/drive/folders/1ZsQjBJJ4UAAp9zrGxm3c4qrhnvGBUYHw































































































































































































