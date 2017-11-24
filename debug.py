#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Try
# 
# try:
# 	print('try:')
# 	r = 10 / 0
# 	print('result:',r)
# except ZeroDivisionError as e:
# 	print('except:',e)
# else:
# 	pass
# finally:
# 	print('finally...')

# print('end')


# Debug

# assert 断言

# def foo(s):
# 	n = int(s)
# 	assert n != 0,'n is zero'
# 	return 10 / n

# def main():
# 	foo('0')

# if __name__ == '__main__':
# 	main()

# logging
# 可指定日志级别 debug,info,warning,error
import logging
logging.basicConfig(level=logging.INFO)

s = '0'
n = int(s)
logging.info('n=%d' %n)
print(10 / n)
# 输出：
# INFO:root:n=0
# Traceback (most recent call last):
#   File "debug.py", line 42, in <module>
#     print(10 / n)
# ZeroDivisionError: division by zero


# 调试器 pdb  可以设置断点
# python -m pdb debug.py
# 命令 l 查看代码
# 命令 n 单步执行代码
# 命令 p 变量名  可查看变量 
# 命令 q 退出
# pdb.set_trace()
# err.py
import pdb

s = '0'
n = int(s)
pdb.set_trace() # 运行到这里会自动暂停
print(10 / n)





