"""
    Tuple
"""

t = ('English', 'History', 'Math')
print(t)             #('English', 'History', 'Math')
print(type(t))       #<class 'tuple'>
print(len(t))        #3

print('\n-----------------------------------------')

print(t[0])            #English
print(t[1:3])          #('History', 'Math')
# t[0] = 'Art'           #TypeError: 'tuple' object does not support item assignment

print('\n-----------------------------------------')

for i in t:
    print(f'I like to raed {i}')

# I like to raed English
# I like to raed History
# I like to raed Math

print('\n-----------------------------------------')

t = (1, 9, 2)
print(sum(t))        #12
print(max(t))        #9
print(min(t))        #1
print(t.count(9))    #1
print(t*2)           #(1, 9, 2, 1, 9, 2)

print('\n-----------------------------------------')

print(tuple(reversed(t)))      #(2, 9, 1)

print('\n-----------------------------------------')

t = (5)
print(type(t))           #<class 'int'>

t = (5,)
print(type(t))           #<class 'tuple'>

t = ('a')
print(type(t))           #<class 'str'>

t = ('a',)
print(type(t))           #<class 'tuple'>

print('\n-----------------------------------------')

t1 = (1, 2)
t2 = (2, 1)
print(t1 == t2)   #False

print('\n-----------------------------------------')

#Append
t = (4, 9)
t = t + (8,)
print(t)         #(4, 9, 8)

#or
t = (4, 9)
a = list(t)
a.append(8)
t = tuple(a)
print(t)        #(4, 9, 8)

print('\n-----------------------------------------')

#Remove
t = (4, 9)
a = list(t)
a.remove(4)
t = tuple(a)
print(t)        #(9,)

print('\n-----------------------------------------')

#Unpack
t = (1, 2)
a, b = t
print(a)     #1
print(b)     #2

print('\n-----------------------------------------')

car = ('blue', '207', 1400)
color, _ , d = car
print(color) #blue
print(_)     #207
print(d)     #1400

print('\n-----------------------------------------')

#Zip
a = (1, 2)
b = (3, 4)
c = zip(a, b)
x = list(c)
print(x)             #[(1, 3), (2, 4)]
print(x[0])          #(1, 3)
print(type(x[0]))    #<class 'tuple'>

print('\n-----------------------------------------')

#Unzip
z = [(1, 3), (2, 4)]
u = zip(*z)
print(list(u))

print('\n-----------------------------------------')

num = [8, 2 , (9, 3), 4, (1, 6, 7), 34]
c = 0
for i in num:
    if isinstance(i, tuple):
        continue
    c += 1

print(c)               #4
print(len(num) - c)    #2

print('\n-----------------------------------------')

a = [(1, 2, 3), (4, 5, 6)]
b = [i[:-1]+(9,) for i in a]
print(b)     #[(1, 2, 9), (4, 5, 9)]

#  دانشگاه شهید مدنی آذربایجان
#  برنامه نویسی مقدماتی با پایتون
#  امین گلزاری اسکوئی
# https://github.com/Amin-Golzari-Oskouei/Python-Programming-Course-Basic-2021
# https://drive.google.com/drive/folders/1ZsQjBJJ4UAAp9zrGxm3c4qrhnvGBUYHw













































































































































































