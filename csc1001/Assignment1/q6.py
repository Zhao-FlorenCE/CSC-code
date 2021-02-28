from math import sin
from math import cos
from math import tan
import sys

def is_trigonometric(x):
    if x == 'sin':
        return 1
    elif x == 'cos':
        return 2
    elif x == 'tan':
        return 3
    else:
        print('Not a valid trigonometric function')
        sys.exit()

def is_int(x):
    try:
        x = int(x)
        return x
    except:
        print('Please enter an integer.')
        sys.exit()

function = is_trigonometric(input("Enter the function name: "))
a = is_int(input('Enter left end point a: '))
b = is_int(input('Enter right end point b: '))
n = is_int(input('Enter number n: '))

sum = 0
if function == 1:
    for i in range(n):
        sum += (b - a) / n * sin(a + (b - a) / n * (i + 1 / 2))
elif function == 2:
    for i in range(n):
        sum += (b - a) / n * cos(a + (b - a) / n * (i + 1 / 2))
elif function == 3:
    for i in range(n):
        sum += (b - a) / n * tan(a + (b - a) / n * (i + 1 / 2))
print('The answer is:',sum)