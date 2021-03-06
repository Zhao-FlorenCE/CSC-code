#输入一个正整数判断是不是素数

from math import sqrt

num = int(input('Number: '))
prime = True
for i in range(2,int(sqrt(num)) + 1):
    if num % i == 0:
        prime = False
        print('False. ')
        break
if prime == True:
    print('True. ')

#输入两个正整数，计算它们的最大公约数和最小公倍数

num1 = int(input('Number1: '))
num2 = int(input('Number2: '))
maxnum = max(num1, num2)
minnum = min(num1, num2)
for i in range(maxnum, 0 ,-1):
    if maxnum % i == 0 and \
    minnum % i == 0:
        print('GCD is', i, end = '')
        print('.')
        print('LCM is',\
            int(num1 * num2 / i), end = '')
        print('.')
        break

#打印三角形图案

row = int(input('Row: '))
print('')
for i in range(row):
    for j in range(i + 1):
        print('*',end = '')
    print('')
print('\n')
for i in range(row):
    for j in range(row - i):
        print(' ', end = '')
    for k in range(row - i, row + 1):
        print('*',end = '')
    print('')
print('\n')
for i in range(row):
    for j in range(row - i - 1):
        print(' ', end = '')
    for j in range(i * 2 + 1):
        print('*', end = '')
    print('')