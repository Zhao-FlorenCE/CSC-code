# Check whether the start match the condition
def is_valid(n):

    if n[0] != '4' and n[0] != '5' and n[0] != '6' and n[:2] != '37':
        return False
    return True

# Check whether the digit match the condition
def get_digit(n):
    
    if 12 < len(n) < 17:
        return True
    return False

# Calculate the sum of double place numbers
def double_place_sum(n):

    double_sum = 0
    for i in range(len(n) - 2, -1, -2):
        double_sum += (2 * int(n[i])) % 10 + (2 * int(n[i])) // 10
    return double_sum

# Calculate the sum of odd place numbers
def odd_place_sum(n):
    
    odd_sum = 0
    for i in range(len(n) - 1, -1, -2):
        odd_sum += int(n[i])
    return odd_sum

# Check if the card number is valid
number = input('Please enter your card number: ')
if is_valid(number) and get_digit(number):
    if (double_place_sum(number) + odd_place_sum(number)) % 10 == 0:
        print('Valid card number.')
    else:
        print('Invalid card number.')
else:
    print('Invalid card number.')