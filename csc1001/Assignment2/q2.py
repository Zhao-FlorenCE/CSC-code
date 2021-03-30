import math

def is_prime(n):

    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True

def is_palindrome(n):

    n = str(n)
    n_reversed = n[::-1]
    if n_reversed == n:
        return True
    return False

def is_reverse_prime(n):

    n_reversed = str(n)[::-1]
    return (is_prime(int(n_reversed)))

n = 13
i = 0
while i < 100:
    i += 1
    if is_prime(n) and is_reverse_prime(n) and not is_palindrome(n):
        print(n, end = '\t')
        if i % 10 == 0:
            print()
    else:
        i -= 1
    n += 1