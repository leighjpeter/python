#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 文件操作
# 读文件
# f = open('test.txt','r')
# f.read()
# f.close()
# read(size)
# readline()
# readlines()
# with open('test.txt','r') as f:
# 	print(f.read())
# 像open函数返回的这种有个read()方法的对象，在Python统称为file-like Object
# 二进制文件
# f = open('test.txt','rb')
# 字符编码问题
# f = open('test.txt','r',encoding='gbk',errors='ignore')

# 写文件 
# f = open('test.txt','w')
# f = open('test.txt','wb')
# f.write()
# f.close()
with open('test.txt','w+') as f:
	f.write('撒旦撒旦sadsdadsda')


# StringIO和BytesIO是在内存中操作str和bytes的方法
from io import StringIO
f = StringIO()
f.write('hello')
f.write(' ')
f.write('world')
print(f.getvalue())


from io import BytesIO
f = BytesIO()
f.write('中文'.encode('utf-8'))
print(f.getvalue())

# os
import os
os.name # operating system
os.environ # 环境变量
os.environ.get('key')

# 操作文件和目录
os.path.abspath('.')
os.path.join('/vagrant','testdir') # /vagrant/testdir
os.mkdir('/vagrant/testdir')
os.rmdir('/vagrant/testdir')

# 路径拆分，合并 不要当字符串去处理
# 路径的拆分，合并 不要求目录和文件真实存在
os.path.join()
os.path.split('/vagrant/testdir') # ('/vagrant', 'testdir')
os.path.splitext('/vagrant/testdir/a.txt') # 获取扩展名 ('/vagrant/testdir/a', '.txt'

# 复制 shutil模块提供了copyfile()的函数
shutil.copy()

[x for x in os.listdir('.') if os.path.isdir(x)]

[x for x in os.listdir('.') if os.path.splitext(x)[1] == '.py']


# 查找文件 searchFile.py









