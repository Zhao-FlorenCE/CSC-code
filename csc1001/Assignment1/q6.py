from math import sin
from math import cos
from math import tan

def is_trigonometric():
    global function
    function = input("Enter the function name: ")
    if function == 'sin':
        function = 1
    elif function == 'cos':
        function = 2
    elif function == 'tan':
        function = 3
    else:
        print('Not a valid trigonometric function')
        return False
    return function

while True:
    if is_trigonometric():
        break
    else:
        continue

def test_a():
    global a
    while True:
        try:
            a = float(input('Enter left end point a: '))
            break
        except:
            print('Please enter a number')

def test_b():
    global b
    while True:
        try:
            b = float(input('Enter right end point b: '))
            break
        except:
            print('Please enter a number')

while True:
    test_a()
    test_b()
    if a >= b:
        print('Number a should be smaller than b')
    else:
        break

while True:
    try:
        n = int(input('Enter number n: '))
    except:
        print('Please enter a positive integer')
        continue
    if n > 0:
        break
    else:
        print('Please enter a positive integer')

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