#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from functools import reduce

def str2float(s):
	def char2num(s):
		return	{'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
	if s.isdigit():
		return float(s)
	i = s.index('.')
	a = s[:i] # 123
	b = s[i+1:] # 456
	return ( reduce(lambda x,y: x * 10 + y,list(map(char2num,a)) ) * pow(10,len(b)) + reduce(lambda x,y: x * 10 + y,map(char2num,b)) ) / pow(10,len(b))

print('str2float(\'123.00\') =', str2float('123')) # 123.0
print('str2float(\'123.34566\') =', str2float('123.34566')) # 123.34566


# isdigit()
# isalpha() 只有字幕组成
# isalnum() 由字母和数字组成