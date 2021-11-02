'''
Control statements:
    if
    if else
    elif
'''

import math
n = -16
if n < 0:
    n = abs(n)

print(math.sqrt(n))     #4.0

print('------------------------------------')

a = 5
if True:
    a = 6
print(a)               #6

print('------------------------------------')

a = 20
if a % 2 ==0:
    print('even')      #even
else:
    print('odd')

print('------------------------------------')

x = 3
y = 2
if x == 1 or y == 1:
    print('OK')
else:
    print('No')        #No

print('------------------------------------')

names = ['sara', 'taha', 'ali']
if 'ali' in names:
    print('found')    #found
else:
    print('not found')

print('------------------------------------')

print('conditional expression')

a = 2
b = 5

if a < b:
    m = a
else:
    m = b

print(m)    #2

m = a if a < b else b

print(m)    #2

print('------------------------------------')

my_lst = ['a', 'e', 'o', 'u', 'i']

if 'o' in my_lst:
    s = 'Yes'
else:
    s = 'No'

print(s)    #yes

s = 'Yes' if ('o' in my_lst) else 'No'
print(s)    #yes

print('------------------------------------')

x = 2
y = 6

z = 1 + (x if x > y else y+2)
print(z)    #9

print('------------------------------------')

grade = 13
s = 'fail' if grade < 10 else 'pass'
print(s)  #pass

print('------------------------------------')

today = 'holiday'
b = 25000

if today == 'holiday':
    if b > 20000:
        print('Shoping')       #Shoping
    else:
        print('Watch TV')
else:
    print('Normal working day')

print('------------------------------------')

score = 75

if score >= 90:
    l = 'A'
else:
    if score >= 80:
        l ='B'
    else:
        if score >= 70:
            l ='C'
        else:
            l = 'D'

print(l)   #c

#or

if score >= 90:
    l = 'A'
elif score >= 80:
    l = 'B'
elif score >= 70:
    l = 'C'
else:
    l = 'D'

print(l)   #c

print('------------------------------------')

x = -2
y = -4

if x > 0 and y > 0:
    print('A')
elif x > 0 and y < 0:
    print('B')
elif y > 0:
    print('C')
else:
    print('D')     #D

print('------------------------------------')
age = 18
gender = 'M'

if age < 23:
    if gender == 'M':
        print('Son')    #Son
    else:
        print('Daughter')
elif age >= 23 and age < 65:
    if gender == 'M':
        print('Father')
    else:
        print('Mother')
else:
    if gender == 'M':
        print('Grandfather')
    else:
        print('Grandmother')

print('------------------------------------')

w = 75
h = 1.75

bmi = w / (h ** 2)

if bmi <=15:
    c = 'Very severely underweight'
elif 15 < bmi <= 16:
    c = 'Severely underweight'
elif 16 < bmi <= 18.5:
    c = 'Underweight'
elif 18.5 < bmi <= 25:
    c = 'Normal'
elif 25 < bmi <= 30:
    c = 'Overweight'
elif 30 < bmi <= 35:
    c = 'Moderataly obese'
elif 35 < bmi <= 40:
    c = 'Severely obese'
elif bmi > 40:
    c = 'obese'

print('Your BMI = ' + str(bmi) + ' You are ' + c + '.')
# Your BMI = 24.772096710265558 You are Normal.

#  دانشگاه شهید مدنی آذربایجان
#  برنامه نویسی مقدماتی با پایتون
#  امین گلزاری اسکوئی
# https://github.com/Amin-Golzari-Oskouei/Python-Programming-Course-Basic-2021
# https://drive.google.com/drive/folders/1ZsQjBJJ4UAAp9zrGxm3c4qrhnvGBUYHw
