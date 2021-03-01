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

while True:
    flag_a = False
    try:
        a = float(input('Enter left end point a: '))
        flag_a = True
    except:
        print('Please enter a number')
        continue
    if flag_a:
        break

while True:
    flag_b = False
    try:
        b = float(input('Enter right end point b: '))
        flag_b = True
    except:
        print('Please enter a number')
        continue
    if flag_b:
        break

while True:
    flag_n = False
    try:
        n = int(input('Enter number n: '))
        flag_n = True
    except:
        print('Please enter an integer')
        continue
    if flag_n:
        break

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