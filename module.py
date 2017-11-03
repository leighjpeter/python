#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 一个.py文件就是一个模块
# 按目录组织模块，称为包
# 每一个包目录下必须有一个__init__.py 文件
# _xxx __xxx 这种是私有变量或函数的命名约定


#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'a test module' # 表示模块的文档注释，任何模块代码的第一个字符串都被视为模块的文档注释；

__author__ = 'leighj' # 特殊变量

import sys

def test():
	args = sys.argv
	if len(args) == 1:
		print('hello world')
	elif len(args) == 2:
		print('hello %s' %args[1])
	else :
		print('Too many arguments')

if __name__ == '__main__':
	test()