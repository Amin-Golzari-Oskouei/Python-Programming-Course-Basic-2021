'''
Text

Binary
'''

f = open('E:/teaching/python/Basic/Pycharm/File/myfile.txt', 'w')
line1 = 'Hello Python\n'
line2 = 'C++\n'
line3 = str(52)
f.write(line1)
f.write(line2)
f.write(line3)
print(f.name)        #E:/teaching/python/Basic/Pycharm/File/myfile.txt
print(f.mode)        #w
f.close()

print('\n---------------------------------')

with open('E:/teaching/python/Basic/Pycharm/File/myfile2.txt', 'w') as myfile:
    line1 = 'Hello Python\n'
    line2 = 'C++\n'
    line3 = str(52)
    myfile.write(line1)
    myfile.write(line2)
    myfile.write(line3)

print('\n---------------------------------')

try:
    f = open('myfile3.txt', 'r')
except FileNotFoundError:
    print('Error')     #Error

print('\n---------------------------------')

with open('myfile2.txt', 'r') as f:
    data = f.readlines()
    print(data)  #['Hello Python\n', 'C++\n', '52']

print('\n---------------------------------')

with open('myfile2.txt') as f:
    data1 = f.readline()
    data2 = f.readline()
    print(data1)    #Hello Python
    print(data2)    #C++

print('\n---------------------------------')

with open('myfile2.txt') as f:
    print(f.readline(3))   #Hel
    print(f.readline(5))   #lo Py

print('\n---------------------------------')

with open('myfile2.txt') as f:
    for line in f:
        print(line, end = '')

# Hello Python
# C++
# 52

print('\n---------------------------------')

with open('myfile2.txt') as f:
    x = f.read()
    print(x)
# Hello Python
# C++
# 52
    print(type(x))  #<class 'str'>

print('\n---------------------------------')

import os
n = 'myfile2.txt'
print(os.path.exists(n))  #true
os.remove(n)

print('\n---------------------------------')

name1 = 'myfile.txt'
name2 = 'a.txt'

with open(name1, 'r') as f1, open(name2, 'w') as f2:
    for line in f1:
        f2.write(line)

print('\n---------------------------------')

name1 = 'x.txt'
name2 = 'y.txt'
name3 = 'z.txt'

with open(name1, 'w') as f1:
    f1.write('ali\n')
    f1.write('sara\n')

with open(name2, 'w') as f2:
    f2.write('amin\n')
    f2.write('taha\n')
    f2.write('mahsa')

with open(name1) as f1, open(name2) as f2:
    data1 = f1.read()
    data2 = f2.read()

with open(name3, 'w') as f3:
    f3.write(data1 + data2)

print('\n---------------------------------')

lst = ['yes', 'no','yes', 'yes', 'no','yes', 'no','yes', 'no']
name = 'answer.txt'

with open(name, 'w') as f:
    for i in lst:
        f.write(i)
        f.write('\n')

print('\n---------------------------------')

c1 = 0
c2 = 0

with open(name, 'r') as f:
    lst = f.readlines()
    for i in lst:
        x = i.strip()
        if x == 'yes':
            c1 += 1
        else:
            c2 += 1

print(c1)  #5
print(c2)  #4

print('\n---------------------------------')

d = dict()
with open(name) as f:
    for line in f:
        w = line.split()
        for i in w:
            d[i] = d.get(i, 0) + 1

print(d)  #{'yes': 5, 'no': 4}

print('\n---------------------------------')

def count(filename):
    try:
        with open(filename, 'r') as f:
            x = f.read()
    except FileNotFoundError as er:
        print(er)
    else:
        c = len(x.split())
        print(f'{filename}: {c}')


count('x.txt')        #2
count('answer.txt')   #9
count('myfile2.txt')  #No such file or directory: 'myfile2.txt'

print('\n---------------------------------')

def count(filename):
    try:
        with open(filename, 'r') as f:
            x = f.read()
    except FileNotFoundError as er:
        print(er)
    else:
        c = len(x.split())
        print(f'{filename}: {c}')

lst = ['x.txt', 'answer.txt', 'myfile2.txt']
for i in lst:
    count(i)

# x.txt: 2
# answer.txt: 9
# [Errno 2] No such file or directory: 'myfile2.txt'

print('\n---------------------------------')

with open('Test.txt', 'w') as myfile:
    myfile.write('ABCDEF')

with open('Test.txt', 'r') as f:
    print(f.tell())   #0
    print(f.read(1))  #A
    f.seek(3)
    print(f.read(2))  # DE
    print(f.tell())   # 5
    print(f.read(1))  # F


print('\n---------------------------------')

with open('Test.txt', 'rb') as f:
    print(f.tell())   # 0
    print(f.read(1))  # b'A'
    f.seek(3)
    print(f.read(2))  # b 'DE'
    print(f.tell())   # 5
    print(f.read(1))  # b 'F'
    f.seek(-5, 2)
    print(f.read(1))  # b'B'

print('\n---------------------------------')

line1 = 'ali\n'
line2 = 'sara\n'
lst = [line1, line2]

with open('g.txt', 'w') as f:
    f.writelines(lst)

line3 = 'amin\n'

with open('g.txt', 'a') as f:
    f.write(line3)

print('\n---------------------------------')

x = b'Amin'
print(x)           #b'Amin'
print(x.decode())  #Amin

b = bytes([65, 97])
print(b)           #b'Aa'
print(b.decode())  #Aa

a = bytearray([65, 97])
print(a)           #bytearray(b'Aa')
print(a.decode())  #Aa

print('\n---------------------------------')

data = 'Hello\nPython'
print(data)
# Hello
# Python

b = bytes(data, 'utf-8')
print(b)  #b'Hello\nPython'

with open('myfilebin.bin', 'wb') as f:
    print(f.write(b))    #12

print('\n---------------------------------')

import json
d = {'k1': 'v1', 'k2':'v2'}

js = json.dumps(d)
print(js)  #{"k1": "v1", "k2": "v2"}

js = json.dumps(d, indent = 4)
print(js)
# {
#     "k1": "v1",
#     "k2": "v2"
# }

js = json.dumps(d, indent = 4, separators = (';', '='))
print(js)
# {
#     "k1"="v1";
#     "k2"="v2"
# }

with open('j.json', 'w') as f:
    json.dump(d, f)

with open('j.json') as f:
    print(json.load(f))    #{'k1': 'v1', 'k2': 'v2'}

print('\n---------------------------------')

import pickle

with open('p.bin', 'wb') as f:
    pickle.dump(d, f)

with open('p.bin', 'rb') as f:
    print(pickle.load(f))    #{'k1': 'v1', 'k2': 'v2'}

print('\n---------------------------------')

import csv
x = ['name', 'age']
r1 = ['ali', 35]
r2 = ['mahsa', 12]
r3 = ['amin', 21]

with open('a.csv', 'w') as f:
    w = csv.writer(f)
    w.writerow(x)
    w.writerows([r1, r2, r3])

with open('a.csv', newline = '\n') as f:
    r = csv.reader(f)
    for i in r:
        print('   '.join(i))

# name   age
# ali   35
# mahsa   12
# amin   21

print('\n---------------------------------')

import pandas as pd

data = pd.read_csv('a.csv')

print(data)

#     name  age
# 0    ali   35
# 1  mahsa   12
# 2   amin   21

data.to_csv('b.csv', sep = ',', index = False)

print('\n---------------------------------')

import glob
print(glob.glob('*.txt'))
#['a.txt', 'answer.txt', 'g.txt', 'myfile.txt', 'Test.txt', 'x.txt', 'y.txt', 'z.txt']

#  دانشگاه شهید مدنی آذربایجان
#  برنامه نویسی مقدماتی با پایتون
#  امین گلزاری اسکوئی
# https://github.com/Amin-Golzari-Oskouei/Python-Programming-Course-Basic-2021
# https://drive.google.com/drive/folders/1ZsQjBJJ4UAAp9zrGxm3c4qrhnvGBUYHw































































