from math import sqrt

def is_num(n):
    try:
        num = int(n)
        return True
    except:
        return False

def is_prime(num):
    prime = True
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            prime = False
            break
    if prime == True:
        return num

num = input('Number: ')

if is_num(num):
    num = int(num)
    
    if num >= 2:
        print('The prime numbers smaller than %d include:' % (num))
        j = 0
        for i in range(1, num):
            if is_prime(i + 1):
                print(is_prime(i + 1), end = '\t')
                j += 1
                if j % 8 == 0:
                    print()
    elif num == 1:
        print('There is no prime number smaller than 1.')
    else:
        print('Please enter a proper number.')
else:
    print('Please enter a integer.')