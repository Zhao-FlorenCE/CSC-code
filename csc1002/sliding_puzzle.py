import os
import time
import random

def start_menu():

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
    game_info()

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
    print('\n')
    input_size()

def game_info_in_game():

    os.system('cls')
    print('===================================================================')
    print('|                                                                 |')
    print('|                                                                 |')
    print('|         _____                        _____        __            |')
    print('|        / ____|                      |_   _|      / _|           |')
    print('|       | |  __  __ _ _ __ ___   ___    | |  _ __ | |_ ___        |')
    print('|       | | |_ |/ _` | `_ ` _ \ / _ \   | | | `_ \|  _/ _ \       |')
    print('|       | |__| | (_| | | | | | |  __/  _| |_| | | | || (_) |      |')
    print('|        \_____|\__,_|_| |_| |_|\___| |_____|_| |_|_| \___/       |')
    print('|                                                                 |')
    print('|                                                                 |')
    print('|                                                                 |')
    print('|          This is a game to rearrange the lost numbers.          |')
    print('|           Use your keyboard to help find their homes.           |')
    print('|                                                                 |')
    print('|                                                                 |')
    print('===================================================================')
    print('\n')

def input_size():

    global size
    while True:
        size = input('Please enter the map size (larger than two and smaller than eleven) > ')
        try:
            size = int(size)
            if (3 <= size <= 10):
                break
            else:
                print('Please enter a number larger than two and smaller than eleven.')
                continue
        except:
            print('Please enter a integer.')
            continue
    bind_keys()

def bind_keys():

    global keys_left, keys_right, keys_up, keys_down
    while True:
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
    game_self()

def game_self():

    global map
    map_size = size ** 2
    map = random.sample(range(map_size), map_size)
    map_test(map)
    #print(map)

def map_test(a):

    global inversion_num, zero_position, zero_position_y, zero_position_x
    is_game_start = False
    inversion_num = 0
    for i in range(len(a)):
        if a[i] == 0:
            zero_position = i
        for j in range(len(a) - i):
            if a[len(a) - 1 - i] < a[j] and a[len(a) - 1 - i] * a[j] != 0:
                inversion_num += 1
    #print(inversion_num)
    #print(zero_position)
    #print(zero_position_y)
    if size % 2 != 0: #size is odd
        if inversion_num % 2 == 0: #inversion number is even
            is_game_start = True
        else:   #inversion number is odd
            is_game_start = False
    else: #size is even
        if inversion_num % 2 == 0: #inversion number is even
            if (size - zero_position) % 2 == 0: #the line difference is even
                is_game_start = True
            else: #the line difference is odd
                is_game_start = False
        else: #inversion number is odd
            if (size - zero_position) % 2 != 0: #the line difference is odd
                is_game_start = True
            else: #the line difference is even
                is_game_start = False
    if is_game_start:
        game_start()
    else:
        game_self()

def game_start():

    os.system('cls')
    game_info_in_game()
    global zero_position
    test_map = [0] * len(map)
    for i in range(len(map) - 1):
        test_map[i] = i + 1
    if test_map == map:
        game_end()
    else:
        for i in range(len(map)):
            if map[i] == 0:
                zero_position = i
                print(' ' ,end = ' ')
            else:
                print(map[i], end = ' ')
            if (i + 1) % size == 0:
                print()
        pre_move()

def pre_move():

    global moveable, is_keys_left, is_keys_right, is_keys_up, is_keys_down
    is_keys_left = is_keys_right = is_keys_up = is_keys_down = False
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
    move()

def move():
    
    move_to = input()
    if move_to == keys_left and is_keys_left:
        map[zero_position] = map[zero_position + 1]
        map[zero_position + 1] = 0
        game_start()
    elif move_to == keys_right and is_keys_right:
        map[zero_position] = map[zero_position - 1]
        map[zero_position - 1] = 0
        game_start()
    elif move_to == keys_up and is_keys_up:
        map[zero_position] = map[zero_position + size]
        map[zero_position + size] = 0
        game_start()
    elif move_to == keys_down and is_keys_down:
        map[zero_position] = map[zero_position - size]
        map[zero_position - size] = 0
        game_start()
    else:
        pre_move()

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
    print('\n')

start_menu()