# file = open('src/Day21-30/abc.txt', 'r', encoding='utf-8')
# print(file.read())
# file.close()


# file = open('src/Day21-30/abc.txt', 'r', encoding='utf-8')
# for line in file:
#     print(line, end='')
# file.close()


# file = open('src/Day21-30/abc.txt', 'a', encoding='utf-8')
# file.write('\n标题：《蜀道难》')
# file.write('\n作者：李白')
# file.close()

# file = None
# try:
#     file = open('src/Day21-30/abc.txt', 'r', encoding='utf-8')
#     print(file.read())
# except FileNotFoundError:
#     print('无法打开指定的文件!')
# except LookupError:
#     print('指定了未知的编码!')
# except UnicodeDecodeError:
#     print('读取文件时解码错误!')
# finally:
#     if file:
#         file.close()


try:
  file1 = open('src/Day21-30/yumaoqiu.jpg', 'rb')
  data = file1.read()
  file1.close()
  file2 = open('src/Day21-30/yumaoqiu_copy.jpg', 'wb')
  file2.write(data)
  file2.close()
except FileNotFoundError:
    print('无法打开指定的文件!')
except IOError:
    print('读写文件时出现错误.')

print('程序执行结束.')