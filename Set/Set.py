"""
    Set
"""

f = {'apple', 'orange', 'grapes'}
print(type(f))           #<class 'set'>
print(len(f))            #3
print(f)                 #{'grapes', 'orange', 'apple'}

print('\n---------------------------------------------------')

for i in f:
    print(i)

print('\n---------------------------------------------------')
f1 = set(('apple', 'orange', 'grapes'))

print(f1)                #{'grapes', 'orange', 'apple'}
print('banana' in f1)    #False

f1.add('cherry')
print(f1)                #{'cherry', 'orange', 'apple', 'grapes'}

f1.update(['mango', 'cherry'])
print(f1)                 #{'orange', 'apple', 'grapes', 'cherry', 'mango'}

f1.remove('apple')
print(f1)                 #{'orange', 'grapes', 'cherry', 'mango'}

f1.update(('mango', 'apple'))
print(f1)                 #{'orange', 'mango', 'cherry', 'grapes', 'apple'}

print('\n---------------------------------------------------')

vowels = {'a', 'e', 'o', 'u', 'i'}
print(vowels)             #{'e', 'u', 'o', 'a', 'i'}

# vowels.remove('k')        #KeyError: 'k
vowels.discard('k')
print(vowels)             #{'e', 'u', 'o', 'a', 'i'}

x = vowels.pop()
print(x)
print(vowels)

c = vowels.copy()
print(c)                 #{'a', 'e', 'i', 'o'}

vowels.clear()
print(vowels)            #set()
print(len(vowels))       #0

del c
# print(c)                #NameError: name 'c' is not defined

print('\n---------------------------------------------------')

#difference
A = {1, 2, 3, 4, 5, 6}
B = {2, 4, 7}

print(A-B)              #{1, 3, 5, 6}
print(B-A)              #{7}

r = A.difference(B)
print(r)                #{1, 3, 5, 6}
print(A)                #{1, 2, 3, 4, 5, 6}
print(B)                #{2, 4, 7}

r = A.difference_update(B)
print(r)                #None
print(A)                #{1, 3, 5, 6}
print(B)                #{2, 4, 7}

X = {1, 2, 3}
Y = {2, 3, 4}
print(X.symmetric_difference(Y))       #{1, 4}
print(X ^ Y)                           #{1, 4}

print('\n---------------------------------------------------')

#intersection

X = {1, 2, 3}
Y = {2, 3, 4}
print(X.intersection(Y))               #{2, 3}
print(X & Y)                           #{2, 3}

print('\n---------------------------------------------------')

#Union

X = {1, 2, 3}
Y = {2, 3, 4}
print(X.union(Y))               #{1, 2, 3, 4}
print(X | Y)                    #{1, 2, 3, 4}

print('\n---------------------------------------------------')

#Union
X = {1, 2, 3}
Y = {2, 3, 4}
X.update(Y)
print(X)                          #{1, 2, 3, 4}

print('\n---------------------------------------------------')

X = {1, 2}
s = 'ali'
a = [13, 22, 'sepideh']
t = (7, 8, 'mahsa')
d = {'one': 10, 'two': 20}

X.update(s,a,t,d)
print(X)         #{1, 2, 'l', 7, 8, 'mahsa', 13, 'i', 'two', 22, 'a', 'one', 'sepideh'}

print('\n---------------------------------------------------')

#isdisjoint
X = {1, 2, 4}
Y = {1, 2, 3}
print(X.isdisjoint(Y))       #False

X = {1, 2, 4}
Y = {5, 6, 3}
print(X.isdisjoint(Y))       #True

print('\n---------------------------------------------------')

#issubset
X = {1, 2}
Y = {1, 2, 3}
print(X.issubset(Y))       #True
print(Y.issubset(X))       #False

print('\n---------------------------------------------------')

w = 'alireza'
x = {'a', 'r'}
s = set(w)
Y = {1, 2, 3}
print(x.intersection(s))       #{'a', 'r'}

print('\n---------------------------------------------------')

d1 = {'a': 1, 'b': 3, 'c': 2}
d2 = {'a': 2, 'b': 3, 'c': 2}

s1 = set(d1.items())
s2 = set(d2.items())
s = s1 & s2

for k,v in s:
    print(k, end =' ')       #c b

print('\n---------------------------------------------------')

#  دانشگاه شهید مدنی آذربایجان
#  برنامه نویسی مقدماتی با پایتون
#  امین گلزاری اسکوئی
# https://github.com/Amin-Golzari-Oskouei/Python-Programming-Course-Basic-2021
# https://drive.google.com/drive/folders/1ZsQjBJJ4UAAp9zrGxm3c4qrhnvGBUYHw

















































































