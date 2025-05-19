# 算术运算符
print(321 + 12)     # 加法运算，输出333
print(321 - 12)     # 减法运算，输出309
print(321 * 12)     # 乘法运算，输出3852
print(321 / 12)     # 除法运算，输出26.75
print(321 // 12)    # 整除运算，输出26
print(321 % 12)     # 求模运算，输出9
print(321 ** 12)    # 求幂运算，输出1196906950228928915420617322241


a = 10
b = 3
a += b        # 相当于：a = a + b
a *= a + 2    # 相当于：a = a * (a + 2)
print(a)      # 大家算一下这里会输出什么

# f = float(input('请输入华氏温度: '))
# c = (f - 32) / 1.8
# print('%.1f华氏度 = %.1f摄氏度' % (f, c))

# f = float(input('请输入华氏温度: '))
# c = (f - 32) / 1.8
# print(f'{f:.1f}华氏度 = {c:.1f}摄氏度')


# radius = float(input('请输入圆的半径: '))
# perimeter = 2 * 3.1416 * radius
# area = 3.1416 * radius * radius
# print('周长: %.2f' % perimeter)
# print('面积: %.2f' % area)

# import math

# radius = float(input('请输入圆的半径: '))
# perimeter = 2 * math.pi * radius
# area = math.pi * radius ** 2
# print(f'周长: {perimeter:.2f}')
# print(f'面积: {area:.2f}')


"""
输入年份，闰年输出True，平年输出False

Version: 1.0
Author: 骆昊
"""
year = int(input('请输入年份: '))
is_leap = year % 4 == 0 and year % 100 != 0 or year % 400 == 0
print(f'{is_leap = }')