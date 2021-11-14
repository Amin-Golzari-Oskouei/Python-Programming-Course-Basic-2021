s = 'abcde'
print(s[1:3])   #bc
print(s[1:-1])  #bcd
print(s[1:4])   #bcd
print(s[::-1])  #edcba
print(s[:4])    #abcd
print(s[1:])    #bcde

print('\n-------------------------------')

s = 'Golzari'
print(len(s))       #7
print(max(s))       #z
print(min(s))       #G
print(ord('G'))     #71
print(chr(71))      #G

print('\n-------------------------------')

s = 'python'

print('py' in s)        #True
print('px' not in s)    #True
print(s == 'Python')    #False
print(s < 'sara')       #True

print(s.islower())      #True
print(s.isupper())      #False

print('\n-------------------------------')

s = 'python3'

print(s.isalnum())      #True
print(s.isalpha())      #False

print('\n-------------------------------')

s = '#python3'

print(s.isalnum())      #False
print(s.isalpha())      #False

print('\n-------------------------------')

s = '123'
print(s.isdigit())      #True
print('\t'.isspace())   #True

print('\n-------------------------------')

s = '21a3bcd4'
k = 0
for ch in s:
    if ch.isdigit() == True:
        k = k + int(ch)

print(k) #10

print('\n-------------------------------')

s = 'welcom to python'

print(s.startswith('welco'))   #True
print(s.endswith('on'))        #True

print(s.find('o'))             #4
print(s.index('o'))            #4

print(s.find('f'))             #-1
# print(s.index('f'))            #ValueError: substring not found

print(s.find('o', 5))          #8
print(s.index('o',10))         #14

s = 'a.golzari@tabrizu.ac.ir'
i = s.find('@')
print(s[i+1:])            #tabrizu.ac.ir

print('\n-------------------------------')

s = 'welcom to python'
print(s.capitalize())     #Welcom to python
print(s.title())          #Welcom To Python

print('\n-------------------------------')

s = 'PyThon'
print(s.lower())        #python
print(s.upper())        #PYTHON
print(s.swapcase())     #pYtHON

print('\n-------------------------------')

s = 'Mohammad Zadeh'
print(s.replace('Zadeh','Nejad'))    #Mohammad Nejad

print('\n-------------------------------')

s = '$$pyt$$hon$$$'
print(s.strip('$'))     #pyt$$hon
print(s.lstrip('$'))    #pyt$$hon$$$
print(s.rstrip('$'))    #$$pyt$$hon

print('\n-------------------------------')

s = '##ali$$'
print(s.lstrip('#').rstrip('$'))   #ali
print(s.strip('$').strip('#'))     #ali

print('\n-------------------------------')

s = 'www.sanjesh.org'

a = s.lstrip('www.')
print(a)     #sanjesh.org

print('\n-------------------------------')

s = 'Python created by Rossum'
a = s.split(' ')
print(a)       #['Python', 'created', 'by', 'Rossum']

print('\n-------------------------------')

b = ['Python', 'created', 'by', 'Rossum']
c = ' '.join(b)
print(c)         #Python created by Rossum

print('\n-------------------------------')

name = 'ali.py'
a = name.split('.')
print(a)            #['ali', 'py']
print(a[1])         #py
print(repr(a[1]))   #'py'

print('\n-------------------------------')

s = 'a.golzari@tabrizu.ac.ir'

u, d = s.split('@')
print(u)   #a.golzari
print(d)   #tabrizu.ac.ir

print('\n-------------------------------')

s = 'ali\nreza'
d = s.split('\n')
print(d)    #['ali', 'reza']

#or

d = s.splitlines()
print(d)    #['ali', 'reza']

print('\n-------------------------------')

s = '127.02.001.0.004'
b = s.split('.')
a = '.'.join([str(int(i)) for i in b])
print(a)     #127.2.1.0.4

#or

f = '001'
print(int(f))         #1
print(str(int(f)))    #1

print('\n-------------------------------')

s = '12'
print(s.zfill(7))   #0000012
print(s.zfill(3))   #0000012

print('\n-------------------------------')

s = 'sara'
print(s.ljust(7, '*'))    #sara***
print(s.rjust(7, '*'))    #***sara
print(s.center(7, '*'))   #**sara*

print('\n-------------Format------------------')

year = 2020
e = 'referendum'

print(f'Results of the {year} {e}')    #Results of the 2020 referendum

print('\n-------------------------------------')

fname = 'Amin'
lname = 'Golzari'

print('name: {0} family: {1}'.format(fname,lname))   #name: Amin family: Golzari
print(f'name: {fname} family: {lname}')              #name: Amin family: Golzari

print('\n-------------------------------------')
s = 'ali'
print(f'name: {s}')       #name: ali
print(f'name: {s!r}')     #name: 'ali'

print('name: {}'.format(s))       #name: ali
print('name: {!r}'.format(s))     #name: 'ali'

print('\n-------------------------------------')

n = 14

print('{:d}'.format(n))      #14
print('{0:d}'.format(n))     #14
print('{0:5d}'.format(n))    #   14

print('\n-------------------------------------')

a = 12
b = 15

print('{0:f} {1:d}'.format(a,b))   #12.000000 15
print('{1:f} {0:d}'.format(a,b))   #15.000000 12
print('{1:d} {0:f}'.format(a,b))   #15 12.000000

print('\n-------------------------------------')

f = 15.999
print('{:.2f}'.format(f))   #16.00

f = -15.999
print('{:.2f}'.format(f))   #-16.00

f = 0.93
print('{:.2%}'.format(f))   #93.00%

f = 20000000
print('{:,}'.format(f))    #20,000,000

print('\n-------------------------------------')

n = 14

print('{:X}'.format(n))      #E
print('{:#X}'.format(n))     #0XE

print('{:b}'.format(n))      #1110
print('{:#b}'.format(n))     #0b1110

print('\n-------------------------------------')

n = 35
print('{:*>6d}'.format(n))    #****35
print('{:*<6d}'.format(n))    #35****
print('{:*^6d}'.format(n))    #**35**

















































































































































































































































