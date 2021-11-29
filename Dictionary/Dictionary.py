"""
   dictionary
"""

d = {'brand': 'cherry',
     'model': 'arizo5',
     'color': 'black'}

print(type(d))        #<class 'dict'>
print(len(d))         #3

#or

d1 = dict(brand='cherry', model='arizo5', color='black')

print(type(d))        #<class 'dict'>
print(len(d))         #3

print('\n-------------------------------------')

d['year'] = 2020
print(d)           #{'brand': 'cherry', 'model': 'arizo5', 'color': 'black', 'year': 2020}
print(d['model'])  #arizo5

print('\n-------------------------------------')

x = d.get('model')
print(x)           #arizo5

print('\n-------------------------------------')

x = d.get('cylinder')
print(x)           #None

x = d.get('cylinder', -1)
print(x)           #-1

# print(d['cylinder'])         #KeyError: 'cylinder'

print('\n-------------------------------------')
print(list(d.keys()))        #['brand', 'model', 'color', 'year']
print(list(d.values()))      #['cherry', 'arizo5', 'black', 2020]
print(list(d.items()))      #[('brand', 'cherry'), ('model', 'arizo5'), ('color', 'black'), ('year', 2020)]

print('\n-------------------------------------')

for k,v in d.items():
     print(k, ': ', v)

# brand :  cherry
# model :  arizo5
# color :  black
# year :  2020

print('\n-------------------------------------')

d.pop('year')
print(d)      #{'brand': 'cherry', 'model': 'arizo5', 'color': 'black'}

print('\n-------------------------------------')

d.popitem()
print(d)      #{'brand': 'cherry', 'model': 'arizo5'}

print('\n-------------------------------------')

d.clear()
print(d)    #{}

print('\n-------------------------------------')

del d
# print(d)    #NameError: name 'd' is not defined

print('\n-------------------------------------')

a = ['x','x','y','z','y']
d = {}

for i in a:
     if i not in d:
          d[i] = 1
     else:
          d[i] += 1

print(d)   #{'x': 2, 'y': 2, 'z': 1}

#or

d1 = {}
for i in a:
     d1[i] = d1.get(i,0) + 1

print(d1)   #{'x': 2, 'y': 2, 'z': 1}

print('\n-------------------------------------')

d2 = d.copy()
print(d2)  #{'x': 2, 'y': 2, 'z': 1}

print('\n-------------------------------------')

s = 'abcdabaif'
d1 = {}
for i in s:
     d1[i] = d1.get(i,0) + 1

print(d1)   #{'a': 3, 'b': 2, 'c': 1, 'd': 1, 'i': 1, 'f': 1}

print('\n-------------------------------------')

line = 'a dictionary is a datastructure'
d = {}
s = line.split()
print(s)         #['a', 'dictionary', 'is', 'a', 'datastructure']

for i in s:
     d[i] = d.get(i,0) + 1

print(d)        #{'a': 2, 'dictionary': 1, 'is': 1, 'datastructure': 1}

print('\n-------------------------------------')

d = {'a':4, 'b':2, 'c':5, 'f':2}

s = 0
for i in d:
     s += d[i]

print(s)      #13

#or

print(sum(d.values()))   #13

print('\n-----------------sort--------------------')

d = {'a':4, 'w':2, 'n':5, 'f':2}

import operator

k = operator.itemgetter(0)
print(sorted(d.items(), key = k))     #[('a', 4), ('f', 2), ('n', 5), ('w', 2)]

k = operator.itemgetter(1)
print(sorted(d.items(), key = k))     #[('w', 2), ('f', 2), ('a', 4), ('n', 5)]

print('\n-------------------------------------')

num = {'ali': [12, 13, 11],
       'mahsa': [15, 10, 14],
       'ata': [10, 9, 20]}

d = {k : sorted(v) for k,v in num.items()}
print(d)           #{'ali': [11, 12, 13], 'mahsa': [10, 14, 15], 'ata': [9, 10, 20]}

print('\n-----------------combine--------------------')
d1 = {'x': 3, 'y': 2, 'z': 1}
d2 = {'w': 5, 't': 2}

d = {}
d = d1.copy()
d.update(d2)
print(d)      #{'x': 3, 'y': 2, 'z': 1, 'w': 5, 't': 2}


print('\n-----------------or--------------------')

d = {}
for i in (d1,d2):
     d.update(i)

print(d)      #{'x': 3, 'y': 2, 'z': 1, 'w': 5, 't': 2}

print('\n-----------------or--------------------')

d = {**d1, **d2}
print(d)      #{'x': 3, 'y': 2, 'z': 1, 'w': 5, 't': 2}

print('\n-------------------------------------')

#map two lists into a dict
k = ['red', 'green']
v = ['#FF0000', '#008000']

z = zip(k, v)
d = dict(z)
print(d)     #{'red': '#FF0000', 'green': '#008000'}

print('\n-------------------------------------')

s = 'alireza'
x = ['a', 'r']
d = {}

for i in s:
     if i in x:
          d.setdefault(i, 0)
          d[i] += 1

print(d)    #{'a': 2, 'r': 1}

print('\n-------------------------------------')

d = {'x': 3, 'x': 2, 'z': 1, 'z': 5, 't': 2}
print(d)     #{'x': 2, 'z': 5, 't': 2}

print('\n-------------------------------------')

d = {'h': 0,
     't': 0}

import random
for i in range(100):
     d[random.choice(list(d.keys()))] += 1

print(d)   #{'h': 48, 't': 52}

print('\n-------------------------------------')

students = [{'id':123, 'name': 'ali', 'pass': True},
            {'id':456, 'name': 'taha', 'pass': False},
            {'id':789, 'name': 'mahsa', 'pass': True},]

print(sum(d['pass'] for d in students))   #2
print(students[0])                        #{'id': 123, 'name': 'ali', 'pass': True}

print('\n------------------Nested dict-------------------')

tel = {'home': '041-4426527',
       'mobile': '0912-4453311'}

person = {'name': 'amin',
          'age': 27,
          'children': ['ali', 'fatemeh'],
          'phone': tel}

print(len(person))                     #4
print(person['phone'])                 #{'home': '041-4426527', 'mobile': '0912-4453311'}
print(person['phone']['mobile'])       #0912-4453311
print(person['children'])              #['ali', 'fatemeh']
print(person['children'][0])           #ali
print(person.pop('age'))               #ali
print(person)
#{'name': 'amin', 'children': ['ali', 'fatemeh'], 'phone': {'home': '041-4426527', 'mobile': '0912-4453311'}}

#  دانشگاه شهید مدنی آذربایجان
#  برنامه نویسی مقدماتی با پایتون
#  امین گلزاری اسکوئی
# https://github.com/Amin-Golzari-Oskouei/Python-Programming-Course-Basic-2021
# https://drive.google.com/drive/folders/1ZsQjBJJ4UAAp9zrGxm3c4qrhnvGBUYHw
































































































































































