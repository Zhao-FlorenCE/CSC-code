import os
import time
import random

def game_menu():

    os.system('cls')
    print('===================================================================');time.sleep(0.008)
    print('|                                                                 |');time.sleep(0.008)
    print('|                                                                 |');time.sleep(0.008)
    print('|    _____ _ _     _ _               _____               _        |');time.sleep(0.008)
    print('|   / ____| |_|   | |_|             |  __ \             | |       |');time.sleep(0.008)
    print('|  | (___ | |_  __| |_ _ __   __ _  | |__) |   _ _______| | ___   |');time.sleep(0.008)
    print('|   \___ \| | |/ _` | | `_ \ / _` | |  ___/ | | |_  /_  / |/ _ \  |');time.sleep(0.008)
    print('|   ____) | | | (_| | | | | | (_| | | |   | |_| |/ / / /| |  __/  |');time.sleep(0.008)
    print('|  |_____/|_|_|\__,_|_|_| |_|\__, | |_|    \__,_/___/___|_|\___|  |');time.sleep(0.008)
    print('|                             __/ |                               |');time.sleep(0.008)
    print('|                            |___/                                |');time.sleep(0.008)
    print('|                                                                 |');time.sleep(0.008)
    print('|                                                                 |');time.sleep(0.008)
    print('|                      Press Enter to Start!                      |');time.sleep(0.008)
    print('|                                                                 |');time.sleep(0.008)
    print('|                                                                 |');time.sleep(0.008)
    print('===================================================================');time.sleep(0.008)
    input()

def game_info():

    os.system('cls')
    print('===================================================================');time.sleep(0.008)
    print('|                                                                 |');time.sleep(0.008)
    print('|                                                                 |');time.sleep(0.008)
    print('|         _____                        _____        __            |');time.sleep(0.008)
    print('|        / ____|                      |_   _|      / _|           |');time.sleep(0.008)
    print('|       | |  __  __ _ _ __ ___   ___    | |  _ __ | |_ ___        |');time.sleep(0.008)
    print('|       | | |_ |/ _` | `_ ` _ \ / _ \   | | | `_ \|  _/ _ \       |');time.sleep(0.008)
    print('|       | |__| | (_| | | | | | |  __/  _| |_| | | | || (_) |      |');time.sleep(0.008)
    print('|        \_____|\__,_|_| |_| |_|\___| |_____|_| |_|_| \___/       |');time.sleep(0.008)
    print('|                                                                 |');time.sleep(0.008)
    print('|                                                                 |');time.sleep(0.008)
    print('|                                                                 |');time.sleep(0.008)
    print('|          This is a game to rearrange the lost numbers.          |');time.sleep(0.008)
    print('|            Use your keyboard to help find their home.           |');time.sleep(0.008)
    print('|                                                                 |');time.sleep(0.008)
    print('|                                                                 |');time.sleep(0.008)
    print('===================================================================');time.sleep(0.008)
    print('')

def game_process():

    global moves

    os.system('cls')
    moves_print = 'You have performed ' + str(moves) +' move'
    if moves > 1:
        moves_print += 's'
    moves_print += '.'
    print('===================================================================')
    print('|                                                                 |')
    print('|                                                                 |')
    print('|                                                                 |')
    print('|           _______                  _ _ _                        |')
    print('|          |__   __|                | | |_|                       |')
    print('|             | |_ __ __ ___   _____| | |_ _ __   __ _            |')
    print('|             | | `__/ _` \ \ / / _ \ | | | `_ \ / _` |           |')
    print('|             | | | | (_| |\ V /  __/ | | | | | | (_| |           |')
    print('|             |_|_|  \__,_| \_/ \___|_|_|_|_| |_|\__, |           |')
    print('|                                                 __/ |           |')
    print('|                                                |___/            |')
    print('|                                                                 |')
    print('|'                   ,moves_print.center(63),                    '|')
    print('|                                                                 |')
    print('|                                                                 |')
    print('===================================================================')
    print('')

def game_end():

    os.system('cls')
    print('===================================================================');time.sleep(0.008)
    print('|                                                                 |');time.sleep(0.008)
    print('|                                                                 |');time.sleep(0.008)
    print('|        _______ _                 _     __     __                |');time.sleep(0.008)
    print('|       |__   __| |               | |    \ \   / /                |');time.sleep(0.008)
    print('|          | |  | |__   __ _ _ __ | | __  \ \_/ /__  _   _        |');time.sleep(0.008)
    print('|          | |  | `_ \ / _` | `_ \| |/ /   \   / _ \| | | |       |');time.sleep(0.008)
    print('|          | |  | | | | (_| | | | |   <     | | (_) | |_| |       |');time.sleep(0.008)
    print('|          |_|  |_| |_|\__,_|_| |_|_|\_\    |_|\___/ \__,_|       |');time.sleep(0.008)
    print('|                                                                 |');time.sleep(0.008)
    print('|                                                                 |');time.sleep(0.008)
    print('|                        Congratulations!                         |');time.sleep(0.008)
    print('|             You helped the numbers find their homes!            |');time.sleep(0.008)
    print('|                                                                 |');time.sleep(0.008)
    print('|                                                                 |');time.sleep(0.008)
    print('===================================================================');time.sleep(0.008)
    print('')
    print('You have totally performed %d moves.\n' % moves)
    print('Do you want to play again?\n\nEnter \'y\' to restart and \'n\' to quit.\n >', end = ' ')
    while True:
        answer = input()
        if answer == 'y':
            is_game_restart = True
            break
        elif answer == 'n':
            is_game_restart = False
            break
        else:
            print('\nPlease enter \'y\' or \'n\'.\n >', end = ' ')
            continue

    return is_game_restart

def map_size():

    global size

    while True:
        size = input('Please enter the map size (larger than two and smaller than eleven) > ')
        try:
            size = int(size)
            if (3 <= size <= 10):
                break
            else:
                print('Please enter a number larger than two and smaller than eleven.\n')
                continue
        except:
            print('Please enter a integer.\n')
            continue

def bind_keys():

    global keys_left, keys_right, keys_up, keys_down

    while True:
        print()
        keys = input('Please enter four different space-separated letters \nfor left, right, up and down moves > ')
        keys_no_space = keys.replace(' ', '')
        if len(keys_no_space) != 4 or len(keys.split()) != len(set(keys.split())):
            continue
        elif not keys_no_space.isalpha():
            continue
        else:
            try:
                keys_left = keys.split()[0]
                keys_right = keys.split()[1]
                keys_up = keys.split()[2]
                keys_down = keys.split()[3]
                break
            except:
                continue

def game_self():

    global map
    map_size = size ** 2

    map = random.sample(range(map_size), map_size)
    map_test()

def map_test():

    global zero_position, moves, is_game_start

    moves = -1
    is_game_start = False
    inversion_num = 0

    for i in range(len(map)):
        if map[i] == 0:
            zero_position = i
        for j in range(len(map) - i):
            if map[len(map) - 1 - i] < map[j] and map[len(map) - 1 - i] * map[j] != 0:
                inversion_num += 1
    if size % 2 != 0:
        if inversion_num % 2 == 0:
            is_game_start = True
        else:
            is_game_start = False
    else:
        if (inversion_num + (size - (zero_position // size + 1))) % 2 == 0:
            is_game_start = True
        else:
            is_game_start = False

def game_start():


    global zero_position, moves, is_game_end

    os.system('cls')

    is_game_end = True
    moves += 1
    test_map = [0] * len(map)
    game_process()

    for i in range(len(map) - 1):
        test_map[i] = i + 1
    if test_map != map:
        for i in range(len(map)):
            if map[i] == 0:
                zero_position = i
                print('  ' ,end = ' ')
            else:
                print('%2d' % map[i], end = ' ')
            if (i + 1) % size == 0:
                print()
        print()
        is_game_end = False
    return is_game_end

def map_move():

    global is_game_end, is_move

    is_keys_left = is_keys_right = is_keys_up = is_keys_down = is_game_end = False
    is_move = True
    zero_position_y = zero_position // size + 1
    zero_position_x = zero_position + 1 - (zero_position_y - 1) * size
    moveable = [1] * (size + 1)
    moveable[1] = 0
    moveable[size] = 2

    print('Please enter your move', end = ' ')
    if moveable[zero_position_x] == 0:
        print('(left - %s,' % keys_left, end = ' ')
        is_keys_left = True
    elif moveable[zero_position_x] == 1:
        print('(left - %s, right - %s,' % (keys_right, keys_left), end = ' ')
        is_keys_left = is_keys_right = True
    elif moveable[zero_position_x] == 2:
        print('(right - %s,' % keys_right, end = ' ')
        is_keys_right = True
    if moveable[zero_position_y] == 0:
        print('up - %s) >' % keys_up, end = ' ')
        is_keys_up = True
    elif moveable[zero_position_y] == 1:
        print('up - %s, down - %s) >' % (keys_down, keys_up), end = ' ')
        is_keys_up = is_keys_down = True
    elif moveable[zero_position_y] == 2:
        print('down - %s) >' % keys_down, end = ' ')
        is_keys_down = True

    move_to = input()
    if move_to == keys_left and is_keys_left:
        map[zero_position] = map[zero_position + 1]
        map[zero_position + 1] = 0
    elif move_to == keys_right and is_keys_right:
        map[zero_position] = map[zero_position - 1]
        map[zero_position - 1] = 0
    elif move_to == keys_up and is_keys_up:
        map[zero_position] = map[zero_position + size]
        map[zero_position + size] = 0
    elif move_to == keys_down and is_keys_down:
        map[zero_position] = map[zero_position - size]
        map[zero_position - size] = 0
    else:
        is_move = False
        print('Sorry, you cannot move in that way.\n')

if __name__ == '__main__':

    while True:
        game_menu()
        game_info()
        map_size()
        bind_keys()
        game_self()

        while not is_game_start:
            game_self()

        game_start()
        map_move()

        while not is_game_end:
            if is_move and game_start():
                break
            else:
                map_move()

        if not game_end():
            break