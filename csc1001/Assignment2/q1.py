import random

def sqrt(last_guess, n):

    next_guess = (last_guess + (n / last_guess)) / 2
    if abs(next_guess - last_guess) < 0.0001:
        return 1, next_guess
    else:
        return 0, next_guess

n = int(input('Please enter a positive number: '))
last_guess = random.uniform(0.0001, n)
while True:
    return_value = sqrt(last_guess, n)
    if return_value[0]:
        print('The approximate square root is:', return_value[1])
        break
    else:
        last_guess = return_value[1]