#实现计算求最大公约数和最小公倍数的函数

def gcd(x, y):
    (x, y) = (y, x) if y < x else (x, y)
    for i in range(x, 0, -1):
        if x % i == 0 and y % i == 0:
            return i 

def lcm(x, y):
    return x * y // gcd(x, y)

#实现判断一个数是不是回文数的函数

def is_palindrome(num):
    num1 = num
    palindrome = 0
    while num1 > 0:
        palindrome = palindrome * 10 + num1 % 10
        num1 //= 10
    return palindrome == num

#实现判断一个数是不是素数的函数

from math import sqrt

def is_prime(num):
    for i in range(2,int(sqrt(num) + 1)):
        if num % i == 0:
            return False
        elif num == 1:
            return False
        else:
            return True

#需要说明的是，
#如果我们导入的模块除了定义函数之外
#还有可以执行的代码，
#那么Python解释器在导入这个模块时
#就会执行这些代码，
#事实上我们可能并不希望如此，
#因此如果我们在模块中编写了执行代码，
#最好是将这些执行代码放入如下所示的条件中，
#这样的话除非直接运行该模块，
#if条件下的这些代码是不会执行的，
#因为只有直接执行的模块的名字才是"__main__"。

'''
def main():
    # Todo: Add your code here
    pass


if __name__ == '__main__':
    main()
'''