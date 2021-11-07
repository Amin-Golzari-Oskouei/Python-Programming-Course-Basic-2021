"""
Loop:
    for
    while
"""

for i in range(4):
    print(i, end = ' ')   #0 1 2 3

print('\n------------------------------')

for i in range(3, 8):
    print(i, end = ' ')   #3 4 5 6 7

print('\n------------------------------')

for i in range(5, 11, 2):
    print(i, end = ' ')   #5 7 9

print('\n------------------------------')

s = 'Python'
for ch in s:
    print(ch)   #P y t h o n

print('\n------------------------------')

for _ in range(3):
    print('Hello', end = ' ')   # Hello Hello Hello

print('\n------------------------------')

for i in range(9, 2, -2):
    print(i, end = ' ')   #9 7 5 3

print('\n------------------------------')

s = 'Python'
c = 0
for _ in s:
    c += 1

print(c)   #6

print('\n------------------------------')

word = 'amin_golzari'
c = 0
for i in word:
    if i == 'a':
        c += 1

print(c)   #2

print('\n------------------------------')

word = 'amin_golzari'
v = 'aeiou'
c = 0
for i in word:
    if i in v:
        print(i, end = ' ')    #a i o a i
        c += 1

print(c)   #5

#or

word = 'amin_golzari'
v = 'aeiou'
a = [i for i in word if i in v]
print(a)    #['a', 'i', 'o', 'a', 'i']

print('\n------------------------------')

for i in range(1, 4):
    for j in range(2, 4):
        print(j, end = ' ')
    print()
# 2 3
# 2 3
# 2 3

'''
i = 1  : j=2 , j=3
i = 2  : j=2 , j=3
i = 3  : j=2 , j=3
'''

print('\n------------------------------')

for i in range(1, 4):
    for j in range(2, 4):
        print(i, end = ' ')
    print()

# 1 1
# 2 2
# 3 3

print('\n------------------------------')

for i in range(2, 5):
    for j in range(i):
        print(j, end = ' ')
    print()

# 0 1
# 0 1 2
# 0 1 2 3

'''
i = 2  : j=0 , j=1
i = 3  : j=0 , j=1 , j=2
i = 4  : j=0 , j=1 , j=2 , j=3
'''
print('\n------------------------------')

for i in range(2, 5):
    for j in range(1 , i):
        print(j, end = ' ')
    print()

# 1
# 1 2
# 1 2 3

'''
i = 2  :  j=1
i = 3  :  j=1 , j=2
i = 4  :  j=1 , j=2 , j=3
'''

print('\n--------------break----------------')

for i in range(5):
    if i == 3:
        break
    else:
        print(i, end =' ')    #0 1 2

print('\n--------------continue----------------')

for i in range(5):
    if i == 3:
        continue
    else:
        print(i, end =' ')   # 0 1 2 4

print('\n------------------------------')

for n in range(10, 15):
    for i in range(2 , n):
        if n % i == 0:
            print(n, end = ' ')
            break

# 10 12 14

'''
n = 10  :  i=2 : 9
n = 11  :  i=2 : 10
n = 12  :  i=2 : 11
n = 13  :  i=2 : 12 
n = 14  :  i=2 : 13
'''
print('\n------------------------------')

for n in range(10, 15):
    for i in range(2 , n):
        if n % i == 0:
            print(n, end = ' ')
            continue

# 10 10 12 12 12 12 14 14

print('\n------------------------------')

for i in range(3, 8):
    for j in range(2 , i):
        if i % j == 0:
            break
        else:
            print(i, end = ' ')

#  3 5 5 5 7 7 7 7 7

'''
i = 3  :  j=2
i = 4  :  j=2 , j=3
i = 5  :  j=2 , j=3 , j=4
i = 6  :  j=2 , j=3 , j=4 , j=5
i = 7  :  j=2 , j=3 , j=4 , j=5 , j=6
'''

print('\n-------------while-----------------')

i = 1
while i <= 3:
    print(i, end =' ')  #1 2 3
    i += 1

print('\n------------------------------')

i = 7
while i >= 3:
    print(i, end =' ')  #7 6 5 4 3
    i -= 1

print('\n------------------------------')

s = 'abcdef'
i = 0
while True:
    if s[i] == 'd':
        break
    print(s[i], end = ' ')   #a b c
    i += 1

print('\n------------------------------')

n = 8
while n > 2:
    n -= 1
    if n == 5:
        break
    print(n, end = ' ')  #7  6

print('\n------------------------------')

n = 8
while n > 2:
    n -= 1
    if n == 5:
        continue
    print(n, end = ' ')  #7  6  4  3  2

print('\n------------------------------')

a = 0
b = 1

while a < 10:
    print (a, end = ' ')   #0  1  2   4   8
    a = b
    b = a + b
'''
a = 0 , b = 1
a = 1 , b = 2
a = 2 , b = 4
a = 4 , b = 8
a = 8 , b = 16
a = 16, b = 32
'''
print('\n------------------------------')

a = 0
b = 1

while a < 10:
    print(a, end=' ')  # 0 1 1 2 3 5 8
    a , b = b , a+b
'''
a = 0 , b = 1
a = 1 , b = 1
a = 1 , b = 2
a = 2 , b = 3
a = 3 , b = 5
a = 5, b = 8
a = 8, b =13
a = 13, b =21
'''
print('\n------------------------------')

import random
n = random.randrange(0 , 10)
f = 'no'
while f == 'no':
    a = int(input('enter: '))
    if a < n:
        print('>')
    elif a > n:
        print('<')
    else:
        print('Correect')
        f = 'yes'

print('Thank you.')

print('\n--------------PEP8----------------')
n = 1
while n<=3: print(n); n+=1


#  دانشگاه شهید مدنی آذربایجان
#  برنامه نویسی مقدماتی با پایتون
#  امین گلزاری اسکوئی
# https://github.com/Amin-Golzari-Oskouei/Python-Programming-Course-Basic-2021
# https://drive.google.com/drive/folders/1ZsQjBJJ4UAAp9zrGxm3c4qrhnvGBUYHw

