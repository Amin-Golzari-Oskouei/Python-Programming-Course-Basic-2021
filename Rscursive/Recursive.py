'''
iterative:
            n! = 1*2*3*...*n

recursive:
            n! = n * (n-1)!
            1! = 1


3! = 3 * 2! = 3 * 2 = 6
2! = 2 * 1! = 2 * 1 = 2
1! = 1

'''

def fact(n):
    f = 1
    if n == 0:
        print('1')
    else:
        for i in range(1, n + 1):
            f *= i
        print(f)

fact(3)  #6

print('\n-----------------------------------------')

'''
recursive:
            n! = n * (n-1)!
            1! = 1
3! = 3 * 2! = 3 * 2 = 6
2! = 2 * 1! = 2 * 1 = 2
1! = 1
'''

def fact_rec(n):
    if n == 1:
        return 1
    else:
        return n * fact_rec(n-1)

print(fact_rec(3))  #6

'''
fact_rec(3) = 3 * fact_rec(2) = 3 * 2 = 6
fact_rec(2) = 2 * fact_rec(1) = 2 * 1 = 2
fact_rec(1) = 1
'''

print('\n-----------------------------------------')

'''
2*3 = 2 + (2*2) = 2 + 4 = 6
2*2 = 2 + (2*1) = 2 + 2 = 4
2*1 = 2
'''

def mul(x, y):
    if y == 0:
        return 0
    elif y == 1:
        return x
    else:
        return x + mul(x, y-1)

print(mul(2, 3))

'''
mul(2, 3) = 2 + mul(2, 2) = 2 + 4 = 6
mul(2, 2) = 2 + mul(2, 1) = 2 + 2 = 4
mul(2, 1) = 2
'''

print('\n-----------------------------------------')

'''
2 ** 3 =  2 * (2**2) = 2 * 4 = 8
2 ** 2 =  2 * (2**1) = 2 * 2 = 4
2 ** 1 =  2
'''

def pow(x, y):
    if y == 0:
        return 1
    elif x == 0:
        return 0
    elif y == 1:
        return x
    else:
        return x * pow(x, y-1)

print(pow(2, 3))          #8

'''
pow(2, 3) = 2 * pow(2, 2) = 2 * 4 = 8
pow(2, 2) = 2 * pow(2, 1) = 2 * 2 = 4
pow(2, 1) = 2
'''

print('\n-----------------------------------------')

# fibonacci (10) : 0, 1, 1, 2, 3, 5, 8
def fibo(n):
    r = []
    a = 0
    b = 1

    while a < n:
        r.append(a)
        a, b  = b , a + b
    return r

print(fibo(10))

print('\n-----------------------------------------')

def fibo(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)

print(fibo(4))          #3
# print(fibo(60))       #...

print('\n-----------------------------------------')

memo = [0] * 200

def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if memo [n] == 0:
        memo[n] = fib(n-1) + fib(n-2)
    return memo[n]

print(fib(4))          #3
print(fib(60))         #1548008755920

print('\n-----------------------------------------')

'''
f([2, 4, 5, 6, 7]) = 2 + f([4, 5, 6, 7]) =2 + 22 = 24
f([4, 5, 6, 7])    = 4 + f([5, 6, 7]) = 4 + 18 = 22
f([5, 6, 7])       = 5 + f([6, 7]) = 5 + 13 = 18
f([6, 7])          = 6 + f([7])  = 6 + 7 = 13
f([7])             = 7 
'''

def f(lst):
    if len(lst) == 1:
        return lst[0]
    else:
        return lst[0] + f(lst[1:])

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f(a))   #55

print('\n-----------------------------------------')

def sum_digit(n):
    if n == 0:
        return 0
    else:
        return n % 10 + sum_digit(n // 10)

print(sum_digit(345))        #12

'''
sum_digits(345) = 5 + sum_digits(34)= 5 + 7 = 12
sum_digits(34)  = 4 + sum_digits(3) = 4 + 3 = 7
sum_digits(3)   = 3 + sum_digits(0) = 3 + 0 = 3
sum_digits(0)   = 0
'''

print('\n-----------------------------------------')

# n + (n-2) + (n-4) + ...
def sum_series(n):
    if n < 1:
        return 0
    else:
        return n + sum_series(n-2)

print(sum_series(10))         #10 + 8 + 6 + 4 + 2 = 30

print('\n-----------------------------------------')

def f(n, base):
    s = '0123456789ABCDEF'
    if n < base:
        return s[n]
    else:
        return f(n//base, base) + s[n % base]

print(f(10,16))       # A
print(f(25,16))       # 19

'''
f(25,16) = f(1,16) + s[9] = 1 + 9 = 19
f(1,16)  = s[1]  = 1
'''

print(f(8,2))         # 1000
'''
f(8,2) = f(4,2) + s[0] = 100 + 0 = 1000
f(4,2) = f(2,2) + s[0] = 10  + 0 = 100
f(2,2) = f(1,2) + s[0] = 1   + 0 = 10
f(1,2) = s[1] =1
'''

print(f(16,16))         # 10

print(f(129,2))         # 10000001

print('\n-----------------------------------------')

def binary_search(lst, x, start = 0, end = None):
    if end is None:
        end = len(lst) - 1
    if start > end:
        return False

    mid = (start + end) // 2

    if x==lst[mid]:
        return mid

    if x < lst[mid]:
        return binary_search(lst, x, start, mid-1)

    if x > lst[mid]:
        return binary_search(lst, x, mid+1, end)

a = [2, 4, 7, 12, 19, 25, 38]
print(binary_search(a, 19))      #4
print(binary_search(a, 4))       #1
print(binary_search(a, 20))      #False




