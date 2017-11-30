#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 正则
# 
# 
import re
# re.match()
# 切分字符串
# re.split(r'[\s\,]+', 'a,b, c  d')
# 分组
# re.group()
# 贪婪匹配
# re.match(r'^(\d+?)(0*)$', '102300').groups() #('1023', '00')

# 编译
re_tel = re.compile(r'^(\d{3})-(\d{3,8})$')
re_tel.match('001-121').groups()

# 作业一验证邮箱
# re_email = re.compile(r'^[a-zA-Z\.]+@[a-zA-Z0-9]+\.[a-zA-Z]{3}$')
# def regEmail(email):
# 	if(re_email.match(email)):
# 		print('%s is a correct email address' %email)
# 	else:
# 		print('%s is a wrong email!!!!!' % email)

# regEmail('someone@gmail.com')
# regEmail('bill.gates@microsoft.com')
