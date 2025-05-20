# languages = ['Python', 'Java', 'C++']
# languages.append('JavaScript')
# print(languages)  # ['Python', 'Java', 'C++', 'JavaScript']
# languages.insert(1, 'SQL')
# print(languages)  # ['Python', 'SQL', 'Java', 'C++', 'JavaScript']


# languages = ['Python', 'SQL', 'Java', 'C++', 'JavaScript']
# if 'Java' in languages:
#     languages.remove('Java')
# if 'Swift' in languages:
#     languages.remove('Swift')
# print(languages)  # ['Python', 'SQL', C++', 'JavaScript']
# languages.pop()
# temp = languages.pop(1)
# print(temp)       # SQL
# languages.append(temp)
# print(languages)  # ['Python', C++', 'SQL']
# languages.clear()
# print(languages)  # []
# languages = ['Python', 'SQL', 'Java', 'C++', 'JavaScript', 'Python']
# languages.remove('Python')
# print(languages)  # ['SQL', 'Java', 'C++', 'JavaScript', 'Python']

# items = ['Python', 'Java', 'Java', 'C++', 'Kotlin', 'Python']
# print(items.index('Python'))     # 0
# # 从索引位置1开始查找'Python'
# print(items.index('Python', 1))  # 5
# print(items.count('Python'))     # 2
# print(items.count('Kotlin'))     # 1
# print(items.count('Swfit'))      # 0
# # 从索引位置3开始查找'Java'
# print(items.index('Java', 3))    # ValueError: 'Java' is not in list

# 场景一：创建一个取值范围在1到99且能被3或者5整除的数字构成的列表。
items = []
for i in range(1, 100):
  if i % 3 == 0 or i % 5 == 0:
    items.append(i)
print(items)

items1 = [i for i in range(1, 100) if i % 3 == 0 or i % 5 == 0]
print(items1)

# 场景二：有一个整数列表nums1，创建一个新的列表nums2，nums2中的元素是nums1中对应元素的平方。
nums1 = [35, 12, 97, 64, 55]
nums2 = []
for num in nums1:
  nums2.append(num ** 2)
print(nums2)

nums3 = [num ** 2 for num in nums1]
print(nums3)

# 场景三： 有一个整数列表nums1，创建一个新的列表nums2，将nums1中大于50的元素放到nums2中。
nums4 = []
for num in nums1:
  if num > 50:
    nums4.append(num)
print(nums4)

nums5 = [num for num in nums1 if num > 50]
print(nums5)

# 如果想通过键盘输入的方式来录入5个学生3门课程的成绩并保存在列表中，可以使用如下所示的代码
# scores = []
# for _ in range(5):
#   _temp = []
#   for _ in range(3):
#     _score = int(input('请输入成绩: '))
#     _temp.append(_score)
#   scores.append(_temp)
# print(scores)

# 如果想通过键盘输入的方式来录入5个学生3门课程的成绩并保存在列表中，可以使用如下所示的代码
import random
scores = [[random.randrange(60, 101) for _ in range(3)] for _ in range(5)]
print(scores)