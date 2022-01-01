# Regular Expressions (Regex)

import re

txt = 'Python is a good programming language.'

m = re.search('good', txt)
print(m)              #<re.Match object; span=(12, 16), match='good'>

m = re.search('are', txt)
print(m)              #None

print('\n---------------------------------')

m = re.search('^is', txt)
print(m)              #None

m = re.search('^Python', txt)
print(m)              #<re.Match object; span=(0, 6), match='Python'>

if (m):
    print('yes')   #yes
else:
    print('No')

print(bool(m))  #True

print('\n---------------------------------')

m = re.search('language.$', txt)
print(m)              #<re.Match object; span=(29, 38), match='language.'>

m = re.search('Python$', txt)
print(m)              #None

print('\n---------------------------------')

x = 'phone number 0949329139 and another 04131234576 number'

m = re.search('number \d+', x)
print(m)       #<re.Match object; span=(6, 23), match='number 0949329139'>

print(m.group(0))      #number 0949329139
# print(m.group(1))    #IndexError: no such group

m = re.search('number (\d+)', x)
print(m)       #<re.Match object; span=(6, 23), match='number 0949329139'>

print(m.group(0))    #number 0949329139
print(m.group(1))    #0949329139

m = re.search('(\w+) (\d+)', x)
print(m)       #<re.Match object; span=(6, 23), match='number 0949329139'>

print(m.group(0))    #number 0949329139
print(m.group(1))    #number
print(m.group(2))    #0949329139

print(re.findall('\d+', x))        #['0949329139', '04131234576']
print(re.findall('\w+ \d+', x))    #['number 0949329139', 'another 04131234576']
print(re.findall('\d+ \w+', x))    #['0949329139 and', '04131234576 number']
print(re.findall('[0-9]', x))
#['0', '9', '4', '9', '3', '2', '9', '1', '3', '9', '0', '4', '1', '3', '1', '2', '3', '4', '5', '7', '6']
print(re.findall('[0-9]+', x))     #['0949329139', '04131234576']
print(re.findall('[0-2]+', x))     #['0949329139', '04131234576']

print('\n---------------------------------')

name = 'Amin Golzari Oskouei'
print(re.findall('f', name))  #[]
print(re.findall('z', name))  #['z']

k = re.findall('[a-m]', name)
print(k)                      #['m', 'i', 'l', 'a', 'i', 'k', 'e', 'i']

print(re.findall('\s+', name))  #[' ', ' ']
print(re.findall('\S+', name))  #['Amin', 'Golzari', 'Oskouei']

print(re.findall('o[^ ]', name))   #['ol', 'ou']
print(re.findall('o[^ ]*', name))  #['olzari', 'ouei']
print(re.findall('o[^e]*', name))  #['olzari Oskou']

print('\n---------------------------------')

e = 'From amin.oskui@gmail.com to a.golzari@tabrizu.ac.ir'
words = e.split()
print(words)   #['From', 'amin.oskui@gmail.com', 'to', 'a.golzari@tabrizu.ac.ir']
print(words[1])  #amin.oskui@gmail.com
print(words[3])  #a.golzari@tabrizu.ac.ir

print(re.findall('\S+@\S+', e))   #['amin.oskui@gmail.com', 'a.golzari@tabrizu.ac.ir']

print(re.split('\s', e))     #['From', 'amin.oskui@gmail.com', 'to', 'a.golzari@tabrizu.ac.ir']
print(re.split('\s', e, 1))  #['From', 'amin.oskui@gmail.com to a.golzari@tabrizu.ac.ir']

print('\n---------------------------------')

txt = 'Python is a good programming language.'

print(re.sub('\s', '_', txt))       #Python_is_a_good_programming_language.
print(re.sub('\s', 'a', txt))       #Pythonaisaaagoodaprogrammingalanguage.
print(re.sub('\S', 'a', txt))       #aaaaaa aa a aaaa aaaaaaaaaaa aaaaaaaaa
print(re.sub('\s', '*', txt, 2))    #Python*is*a good programming language.

print('\n---------------------------------')

phone= '0914-332-32-23'
print(re.sub('\d', '*', phone))  #****-***-**-**
print(re.sub('\D', '*', phone))  #0914*332*32*23

print('\n---------------------------------')

p = '   am in    '
print(re.sub('^\s+', '', p))   #am in
print(re.sub('\s+$', '', p))   #   am in

print('\n---------------------------------')

s = 'ABCDEFCGH'
print(re.sub('CD', 'X', s))   #ABXEFCGH
print(re.subn('C', 'X', s))   #('ABXDEFXGH', 2)

print('\n---------------------------------')

s = 'ABCDEFCGH'
f = re.search('CDE',s)
print(f)    #<re.Match object; span=(2, 5), match='CDE'>
a = f.start()  #2
b = f.end()    #5

k = s[:a] + s[b:]
print(k)     #ABFCGH

print('\n---------------------------------')

text = 'He was carefully disguised but captured quickly by police'
t = re.findall('\w+ly', text)
print(t)    #['carefully', 'quickly']

t = re.finditer('\w+ly', text)
for m in t:
    print(m.start(), m.end(), m.group(0))

# 7 16 carefully
# 40 47 quickly

print('\n---------------------------------')

from typing import NamedTuple

class Token(NamedTuple):
    type: str
    value: str
    line: int
    column: int

def tokenize(code):
    keywords = {'IF', 'THEN', 'ENDIF'}
    token_specification = [
        ('NUMBER',   r'\d+(\.\d*)?'),  # Integer or decimal number
        ('ASSIGN',   r':='),           # Assignment operator
        ('END',      r';'),            # Statement terminator
        ('ID',       r'[A-Za-z]+'),    # Identifiers
        ('OP',       r'[+\-*/]'),      # Arithmetic operators
        ('NEWLINE',  r'\n'),           # Line endings
        ('SKIP',     r'[ \t]+'),       # Skip over spaces and tabs
        ('MISMATCH', r'.'),            # Any other character
    ]
    tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in token_specification)
    line_num = 1
    line_start = 0
    for mo in re.finditer(tok_regex, code):
        kind = mo.lastgroup
        value = mo.group()
        column = mo.start() - line_start
        if kind == 'NUMBER':
            value = float(value) if '.' in value else int(value)
        elif kind == 'ID' and value in keywords:
            kind = value
        elif kind == 'NEWLINE':
            line_start = mo.end()
            line_num += 1
            continue
        elif kind == 'SKIP':
            continue
        elif kind == 'MISMATCH':
            raise RuntimeError(f'{value!r} unexpected on line {line_num}')
        yield Token(kind, value, line_num, column)

statements = '''
    IF quantity THEN
        total := total + price * quantity;
        tax := price * 0.05;
    ENDIF;
'''

for token in tokenize(statements):
    print(token)


#  دانشگاه شهید مدنی آذربایجان
#  برنامه نویسی مقدماتی با پایتون
#  امین گلزاری اسکوئی
# https://github.com/Amin-Golzari-Oskouei/Python-Programming-Course-Basic-2021
# https://drive.google.com/drive/folders/1ZsQjBJJ4UAAp9zrGxm3c4qrhnvGBUYHw

