#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 处理进度
# @param int max 最大值
# @param int current 当前值
# 
import math
def progress(max, current):
	p = 0
	if current:
		p = round(current / max * 100, 2)
	print("progress: [%-50s] %d%%\r" %( '#'[:] * math.ceil(p/2),p ))
	if current == max :
		print("\n")
	
progress(100,50)