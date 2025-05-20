# # 通过关键字def定义求阶乘的函数
# # 自变量（参数）num是一个非负整数
# # 因变量（返回值）是num的阶乘
# def fac(num):
#     result = 1
#     for n in range(2, num + 1):
#         result *= n
#     return result

# m = int(input('m = '))
# print(fac(m))


# # 用星号表达式来表示args可以接收0个或任意多个参数
# # 调用函数时传入的n个参数会组装成一个n元组赋给args
# # 如果一个参数都没有传入，那么args会是一个空元组
# def add(*args):
#     total = 0
#     # 对保存可变参数的元组进行循环遍历
#     for val in args:
#         # 对参数进行了类型检查（数值型的才能求和）
#         if type(val) in (int, float):
#             total += val
#     return total


# # 在调用add函数时可以传入0个或任意多个参数
# print(add())         # 0
# print(add(1))        # 1
# print(add(1, 2, 3))  # 6
# print(add(1, 2, 'hello', 3.45, 6))  # 12.45

# def foo():
#     print('hello, world!')


# def foo():
#     print('goodbye, world!')

    
# foo()  # 大家猜猜调用foo函数会输出什么