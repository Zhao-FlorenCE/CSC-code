#在屏幕上显示跑马灯文字

import os 
import time

def words():
    content = input("Content: ")
    while True:
        os.system('cls')
        print(content)
        time.sleep(0.2)
        content = content[1:] + content[0]


#设计一个函数产生指定长度的验证码，
#验证码由大小写字母和数字构成

import random

def pin_code():
    all_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    length = int(input('Code length: '))
    code = ''
    for i in range(length):
        num = random.randint(0,length - 1)
        code += all_chars[num]
    print('Code: ',code)

#设计一个函数返回给定文件名的后缀名

def file():
    filename = input('Filename: ')
    pos = filename.rfind('.')
    if 0 < pos < len(filename) - 1:
        return filename[pos + 1:]
    else:
        return 'Null'

#设计一个函数返回传入的列表中最大和第二大的元素的值

def list_rank(x):
    x_new = sorted(x, reverse= True)
    a = x_new[0]
    b = x_new[1]
    return a, b

#计算指定的年月日是这一年的第几天

def leap(year):
    return year % 4 == 0 and \
        year % 100 != 0 or \
            year % 400 == 0
def dday(year,month,day):
    days = [
    [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
    [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
][leap(year)]
    total = 0
    for num in range(month - 1):
        total += days[num]
    return total + day

#打印杨辉三角

def yang_hui(row):
    yh = [[]] * row
    for yh_row in range(len(yh)):
        yh[yh_row] = [None] * (yh_row + 1)
        for col in range(len(yh[yh_row])):
            if col == 0 or col == yh_row:
                yh[yh_row][col] = 1
            else:
                yh[yh_row][col] = yh[yh_row - 1][col] + \
                yh[yh_row -1][col - 1]
            print(yh[yh_row][col], end = '\t')
        print()