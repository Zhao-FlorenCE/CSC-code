length = float(input('Length: '))
unit = input('Unit: ')
if unit == 'in':
    print('%f in = %f cm' % (length, length * 2.54))
elif unit == 'cm':
    print('%f cm = %f in' % (length, length / 2.54))
else:
    print('Wrong unit!')

#

score = float(input('Score: '))
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'E'
print('Grade: ',grade)

#

a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))
if a + b > c and a + c > b and b + c > a:
    print('C = %f' % (a + b + c))
    p = (a + b + c) / 2
    print('S = %f' % ((p * (p - a) * (p - b) * (p - c)) ** 0.5))
else:
    print('Not available!')