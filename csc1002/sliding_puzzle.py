import os
import time
import random

def start_menu():

    os.system('cls')
    print('===================================================================');time.sleep(0.01)
    print('|                                                                 |');time.sleep(0.01)
    print('|                                                                 |');time.sleep(0.01)
    print('|    _____ _ _     _ _               _____               _        |');time.sleep(0.01)
    print('|   / ____| |_|   | |_|             |  __ \             | |       |');time.sleep(0.01)
    print('|  | (___ | |_  __| |_ _ __   __ _  | |__) |   _ _______| | ___   |');time.sleep(0.01)
    print('|   \___ \| | |/ _` | | `_ \ / _` | |  ___/ | | |_  /_  / |/ _ \  |');time.sleep(0.01)
    print('|   ____) | | | (_| | | | | | (_| | | |   | |_| |/ / / /| |  __/  |');time.sleep(0.01)
    print('|  |_____/|_|_|\__,_|_|_| |_|\__, | |_|    \__,_/___/___|_|\___|  |');time.sleep(0.01)
    print('|                             __/ |                               |');time.sleep(0.01)
    print('|                            |___/                                |');time.sleep(0.01)
    print('|                                                                 |');time.sleep(0.01)
    print('|                                                                 |');time.sleep(0.01)
    print('|                      Press Enter to Start!                      |');time.sleep(0.01)
    print('|                                                                 |');time.sleep(0.01)
    print('|                                                                 |');time.sleep(0.01)
    print('===================================================================');time.sleep(0.01)
    input()
    game_info()

def game_info():

    os.system('cls')
    print('===================================================================');time.sleep(0.01)
    print('|                                                                 |');time.sleep(0.01)
    print('|                                                                 |');time.sleep(0.01)
    print('|         _____                        _____        __            |');time.sleep(0.01)
    print('|        / ____|                      |_   _|      / _|           |');time.sleep(0.01)
    print('|       | |  __  __ _ _ __ ___   ___    | |  _ __ | |_ ___        |');time.sleep(0.01)
    print('|       | | |_ |/ _` | `_ ` _ \ / _ \   | | | `_ \|  _/ _ \       |');time.sleep(0.01)
    print('|       | |__| | (_| | | | | | |  __/  _| |_| | | | || (_) |      |');time.sleep(0.01)
    print('|        \_____|\__,_|_| |_| |_|\___| |_____|_| |_|_| \___/       |');time.sleep(0.01)
    print('|                                                                 |');time.sleep(0.01)
    print('|                                                                 |');time.sleep(0.01)
    print('|                                                                 |');time.sleep(0.01)
    print('|          This is a game to rearrange the lost numbers.          |');time.sleep(0.01)
    print('|            Use your keyboard to help find their home.           |');time.sleep(0.01)
    print('|                                                                 |');time.sleep(0.01)
    print('|                                                                 |');time.sleep(0.01)
    print('===================================================================');time.sleep(0.01)
    print('\n\n')
    input_size()

def input_size():

    global size
    while True:
        size = input('Please enter the map size (larger than two and smaller than eleven) > ')
        try:
            size = int(size)
            if (size >= 3 and size <= 10):
                break
            else:
                print('Please enter a number larger than two and smaller than eleven.')
                continue
        except:
            print('Please enter a integer.')
            continue
    bind_keys()

def bind_keys():

    keys = input('Please enter four different space-separated letters \nfor left, right, up and down moves > ')
    keys_no_space = keys.replace(' ', '')
    if len(keys_no_space) != 4 or len(keys.split()) != len(set(keys.split())):
        bind_keys()
    elif not keys_no_space.isalpha():
        bind_keys()
    else:
        try:
            keys_left = keys.split()[0]
            keys_right = keys.split()[1]
            keys_up = keys.split()[2]
            keys_down = keys.split()[3]
            game_self()
        except:
            bind_keys()

def game_self():

    global map
    map_size = size ** 2
    map = random.sample(range(map_size), map_size)
    map_test(map)
    #print(map)

def map_test(a):

    global inversion_num, zero_position, zero_position_y, zero_positon_X
    is_game_start = False
    inversion_num = 0
    for i in range(len(a)):
        if a[i] == 0:
            zero_position = i + 1
        for j in range(len(a) - i):
            if a[len(a) - 1 - i] < a[j] and a[len(a) - 1 - i] * a[j] != 0:
                inversion_num += 1
    #print(inversion_num)
    #print(zero_position)
    zero_position_y = zero_position // size + 1
    zero_position_x = zero_position % size
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

    for i in range(len(map)):
        print(map[i], end = ' ')
        if (i + 1) % size == 0:
            print()
    move()