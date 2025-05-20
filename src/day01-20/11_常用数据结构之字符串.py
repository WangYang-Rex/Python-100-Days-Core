# s1 = 'hello, world!'
# s2 = "你好，世界！❤️"
# s3 = '''hello,
# wonderful
# world!'''
# print(s1)
# print(s2)
# print(s3)

# s1 = '\'hello, world!\''
# s2 = '\\hello, world!\\'
# print(s1)
# print(s2)

# s1 = '\it \is \time \to \read \now'
# s2 = r'\it \is \time \to \read \now'
# print(s1)
# print(s2)

# # 拼接和重复
# s1 = 'hello' + ', ' + 'world'
# print(s1)    # hello, world
# s2 = '!' * 3
# print(s2)    # !!!
# s1 += s2
# print(s1)    # hello, world!!!
# s1 *= 2
# print(s1)    # hello, world!!!hello, world!!!


# s = 'abc123456'
# n = len(s)
# print(s[0], s[-n])    # a a
# print(s[n-1], s[-1])  # 6 6
# print(s[2], s[-7])    # c c
# print(s[5], s[-4])    # 3 3
# print(s[2:5])         # c12
# print(s[-7:-4])       # c12
# print(s[2:])          # c123456
# print(s[:2])          # ab
# print(s[::2])         # ac246
# print(s[::-1])        # 654321cba


# 遍历
# s = 'hello'
# for i in range(len(s)):
#     print(s[i])

# s = 'hello'
# for elem in s:
#     print(elem)


# # 大小写
# s1 = 'hello, world!'
# # 字符串首字母大写
# print(s1.capitalize())  # Hello, world!
# # 字符串每个单词首字母大写
# print(s1.title())       # Hello, World!
# # 字符串变大写
# print(s1.upper())       # HELLO, WORLD!
# s2 = 'GOODBYE'
# # 字符串变小写
# print(s2.lower())       # goodbye
# # 检查s1和s2的值
# print(s1)               # hello, world
# print(s2)               # GOODBYE

# 字符串查找
# s = 'hello, world!'
# print(s.find('or'))      # 8
# print(s.find('or', 9))   # -1
# print(s.find('of'))      # -1
# print(s.index('or'))     # 8
# print(s.index('or', 9))  # ValueError: substring not found

# s1 = '   jackfrued@126.com  '
# print(s1.strip())      # jackfrued@126.com
# s2 = '~你好，世界~'
# print(s2.lstrip('~'))  # 你好，世界~
# print(s2.rstrip('~'))  # ~你好，世界

# s = 'hello, good world'
# print(s.replace('o', '@'))     # hell@, g@@d w@rld
# print(s.replace('o', '@', 1))  # hell@, good world

a = '骆昊'
b = a.encode('utf-8')
c = a.encode('gbk')
print(b)                  # b'\xe9\xaa\x86\xe6\x98\x8a'
print(c)                  # b'\xc2\xe6\xea\xbb'
print(b.decode('utf-8'))  # 骆昊
print(c.decode('gbk'))    # 骆昊
