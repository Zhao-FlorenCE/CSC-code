#寻找水仙花数

for num in range(100, 1000):
    if num == (num % 10) ** 3 \
    + (num // 10 % 10) ** 3 + (num // 100) ** 3:
        print(num) 

#百钱百鸡问题

for i in range(0, 20):
    for j in range(0, 33):
        if 5 * i + 3 * j \
        + (100 - i - j) / 3 == 100:
            print('Rooster: %d, Hen: %d, Chicken: %d'\
            % (i, j, 100 - i - j))

#CRAPS赌博游戏

from random import randint

money = 1000
cur_round = 1
max_money = money
while money > 0:
    print('Money: %d, Round: %d' \
        % (money,cur_round))
    go_on = False
    while True:
        debt = int(input('Debt: '))
        if 0 < debt < money:
            break
        elif debt == money:
            print('You are brave to all in!')
            break
        else:
            print('Wrong debt! \
You do not have enough money!')
    first = randint(1, 6) + randint(1, 6)
    print('First roll: ', first)
    if first == 7 or first == 11:
        print('You win!')
        money += debt
    elif first == 2 or first == 3 or \
        first == 12:
            print('You lose!')
            money -= debt
    else:
        go_on = True
    while go_on:
        go_on = False
        next_roll = randint(1, 6) \
            + randint(1, 6)
        print('Next roll: ', next_roll)
        if next_roll == 7:
            print('You lose!')
            money -= debt
        elif next_roll == first:
            print('You win!')
            money += debt
        else:
            go_on = True
    cur_round += 1
    max_money = max(max_money, money)
print('Out of money. You lost!')
print('Total round: %d' % (cur_round - 1))
print('Maxmium Money: ',max_money)