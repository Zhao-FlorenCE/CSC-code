#华氏温度转换为摄氏温度

f = float(input('F: '))
c = (f - 32) / 1.8
print('%.1f F = %.1f C' % (f, c))

#输入圆的半径计算计算周长和面积

r = float(input('Radius: '))
c = 2 * 3.1416 * r
s = 3.1416 * (r ** 2)
print('C = %.2f, S = %.2f' % (c, s))

#输入年份判断是不是闰年

y = int(input('Year: '))
leap = y % 4 == 0 and y % 100 != 0 or \
y % 400 == 0
print(leap)
#比较运算符会产生布尔值
#而逻辑运算符and和or会对这些布尔值进行组合，
#最终也是得到一个布尔值.