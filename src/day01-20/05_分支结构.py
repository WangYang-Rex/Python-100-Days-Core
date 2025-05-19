# height = float(input('身高(cm)：'))
# weight = float(input('体重(kg)：'))
# bmi = weight / (height / 100) ** 2
# print(f'{bmi = :.1f}')
# if 18.5 <= bmi < 24:
#   print('你的身材很棒！')


# height =float(input('请输入身高：'))
# weight = float(input('请输入体重：'))
# bmi = weight / (height / 100) ** 2
# print(f'bmi={bmi:.2f}')
# if bmi < 18.5:
#     print('你的体重过轻！')
# elif bmi < 24:
#     print('你的身材很棒！')
# elif bmi < 27:
#     print('你的体重过重！')
# elif bmi < 30:
#     print('你已轻度肥胖！')
# elif bmi < 35:
#     print('你已中度肥胖！')
# else:
#     print('你已重度肥胖！')

# status_code = int(input('请输入响应状态码：'))
# # match status_code:
# # 	case 400: description = '请求错误'
# # 	case 401: description = '未授权'
# # 	case _: description = 'Unknown Status Code'
# if status_code == 400:
#   description = '请求错误'
# elif status_code == 401:
#   description = '未授权'
# else:
#   description = 'Unknown Status Code'
# print(description)
    
# x = float(input('x = '))
# if x > 1:
#   y = 3 * x - 5
# elif x >= -1:
#   y = x + 2
# else:
#   y = 5 * x + 3
# print(f'y = {y}')
# # print(f'f(x) = {y}')

# 例子3：计算三角形的周长和面积
a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))
if a+b>c and a+c > b and b+c>a:
  print(f'三角形周长：{a+ b+c}')
  s = (a+b+c)/2
  area = (s*(s-a)*(s-b)*(s-c))**0.5
  print(f'三角形面积：{area:.2f}')
else:
  print('不能构成三角形')