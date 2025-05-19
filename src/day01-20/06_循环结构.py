import time

# for i in range(36):
#   print(f'hello, world {i}')
#   time.sleep(1)
# s = range(36)
# print(s)
# print(2 in s)
# print(245 in s)

# sum1 = 0
# sum2 = 0
# for i in range(1, 101):
#   sum1 += i
#   if i % 2 == 0:
#     sum2 +=i
# print(f'1到100的和是：{sum1}')
# print(f'1到100的偶数和是：{sum2}')

# sum_1 = sum(range(1, 101))
# sum_2 = sum(range(2, 101, 2))
# print(f'1到100的和是：{sum_1}')
# print(f'1到100的偶数和是：{sum_2}')

# total = 0
# total2 = 0
# i = 0
# while i < 101:
#   total += i
#   i += 1
#   if i % 2 == 0:
#     total2 += i
# print(f'1到100的和是：{total}')
# print(f'1到100的偶数和是：{total2}')

# 99乘法表
# for i in range(1, 10):
#   for j in range(1, i+1):
#     print(f'{i}*{j}={i*j}', end='\t')
#   print()


# 素数
# num = int(input('请输入一个正整数：'))
# is_prime = True
# end = int(num ** 0.5)
# for i in range(2,end+1):
#   if num % i == 0:
#     is_prime = False
#     break
#   else:
#     continue
# if is_prime:
#   print(f'{num}是素数')
# else:
#   print(f'{num}不是素数')

# 最大公约数
# x = int(input('请输入一个正整数：'))
# y = int(input('请输入一个正整数：'))
# for i in range(x, 0, -1):
#   if x % i == 0 and y % i == 0:
#     print(f'{x}和{y}的最大公约数是：{i}')
#     break

# 猜数字小游戏
import random

answer = random.randrange(1, 101)
counter = 0
while True:
  counter += 1
  num = int(input('请输入：'))
  if num < answer:
    print('大一点')
  elif num > answer:
    print('小一点')
  else:
    print('猜对了')
    break
print(f'你总共猜了{counter}次')