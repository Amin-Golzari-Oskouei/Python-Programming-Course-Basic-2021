# lambda

def f(n):
    return n * 2

print(f(3))   #6

#or

f = lambda n : n * 2
print(f(3))  #6

print('\n---------------------------------')

add = lambda x, y : x + y
print(add(2, 3))     #5

print('\n---------------------------------')

add = lambda x, y : (x + y , x -y)
print(add(2, 3))     #(5, -1)

print('\n---------------------------------')

m = lambda : print('Python')
m()

print('\n---------------------------------')

d = {'a': 3, 'b': 7, 'c': 5}
print(d[max(d.keys() , key = (lambda k: d[k]))])   #7

print('\n---------------------------------')

lst = ['ali', 'reza']
u = []
for i in lst:
    x = i.upper()
    u.append(x)
print(u)       #['ALI', 'REZA']

#or
print('\n----------------Map-----------------')

lst = ['ali', 'reza']
print(list(map(str.upper, lst)))   #['ALI', 'REZA']

print('\n---------------------------------')

name = ['ali', 'reza']
score = [13, 18]

print(list(zip(name, score)))                       #[('ali', 13), ('reza', 18)]
#or
print(list(map(lambda x, y: (x, y), name, score)))  #[('ali', 13), ('reza', 18)]

print('\n---------------------------------')

lst = ['a', 'A']
x = []

for i in lst:
    x.append(ord(i))

print(x)                    #[97, 65]

#or
print(list(map(ord, lst)))  #[97, 65]

print('\n---------------------------------')

score = [12, 15, 9, 8, 11, 20, 7]
print(list(map(lambda x: x>9 , score)))   #[True, True, False, False, True, True, False]

print('\n---------------------------------')

a = [3, 2, 1]
b = [6, 4, 7]

print(list(map(lambda x, y : x + y, a , b)))  #[9, 6, 8]

print('\n---------------------------------')

def f(x):
    return x + 3

def g(y):
    return y * 2

funcs = [f, g]
lst = [1, 2, 3]

for i in lst:
    print(list(map(lambda a: a(i) , funcs)))

# [4, 2]
# [5, 4]
# [6, 6]

print('\n---------------Filter------------------')

score = [12, 15, 9, 8, 11, 20, 7]
print(list(filter(lambda x: x>9 , score)))   #[12, 15, 11, 20]

print('\n---------------------------------')

lst = ['radar', 'madam', 'php', 'ali']
f = lambda x : (x == ''.join(reversed(x)))
print(list(filter(f, lst)))                 #['radar', 'madam', 'php']

print('\n---------------------------------')

lst = [2, 7, '', {}, 5, 6 ,[]]
print(list(filter(None, lst)))     #[2, 7, 5, 6]

print('\n----------------Reduce-----------------')

from functools import reduce

lst = [4, 8, 3, 5]

add = lambda a, b : a + b

print(reduce(add, lst))   #20   (((4 + 8) + 3) + 5)

#or

def my_reduce(func, seq):
    r = seq [0]
    for i in seq[1:]:
        r = func(r, i)
    return r
print(my_reduce(add, lst)) #20

print('\n---------------sorted------------------')

lst = [5, 2, 10, 1, 4, 6]
print(sorted(lst))    #[1, 2, 4, 5, 6, 10]

print('\n---------------------------------')

students = [{'id': 1, 'name' : 'taha', 'score' : 19},
            {'id': 2, 'name' : 'sara', 'score' : 8},
            {'id': 3, 'name' : 'omid', 'score' : 15},
            {'id': 4, 'name' : 'mahsa', 'score' : 19}]
print(sorted(students, key = lambda x : x['name']))

# [{'id': 2, 'name': 'sara', 'score': 8},
#  {'id': 3, 'name': 'omid', 'score': 15},
#  {'id': 1, 'name': 'taha', 'score': 19},
#  {'id': 4, 'name': 'mahsa', 'score': 19}]

students = [{'id': 1, 'name' : 'taha', 'score' : 19},
            {'id': 2, 'name' : 'sara', 'score' : 8},
            {'id': 3, 'name' : 'omid', 'score' : 15},
            {'id': 4, 'name' : 'mahsa', 'score' : 19}]
print(sorted(students, key = lambda x : x['name']))

# [{'id': 4, 'name': 'mahsa', 'score': 19},
# {'id': 3, 'name': 'omid', 'score': 15},
# {'id': 2, 'name': 'sara', 'score': 8},
# {'id': 1, 'name': 'taha', 'score': 19}]

print('\n---------------------------------')

students = [(1, 'taha', 19),
            (2, 'sara',  8) ,
            (3, 'omid',  15),
            (4, 'mahsa', 19)]

from operator import itemgetter

print(sorted(students, key = itemgetter(2)))
# [(2, 'sara', 8),
# (3, 'omid', 15),
# (1, 'taha', 19),
# (4, 'mahsa', 19)]

print(sorted(students, key = itemgetter(2, 1)))
# [(2, 'sara', 8),
# (3, 'omid', 15),
# (4, 'mahsa', 19),
# (1, 'taha', 19)]

print(sorted(students, key = itemgetter(2), reverse=True))
# [(1, 'taha', 19),
# (4, 'mahsa', 19),
# (3, 'omid', 15),
# (2, 'sara', 8)]

print('\n---------------------------------')

d = {'ali' : 13, 'sara' : 17, 'taha' : 15}
print(sorted(d.items(), key = lambda x : x[1]))
# [('ali', 13),
# ('taha', 15),
# ('sara', 17)]

#  دانشگاه شهید مدنی آذربایجان
#  برنامه نویسی مقدماتی با پایتون
#  امین گلزاری اسکوئی
# https://github.com/Amin-Golzari-Oskouei/Python-Programming-Course-Basic-2021
# https://drive.google.com/drive/folders/1ZsQjBJJ4UAAp9zrGxm3c4qrhnvGBUYHw



















































