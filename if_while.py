#!/usr/bin/env python3
# -*- coding: utf-8 -*-
a=input('请输入检测BMI的名字:')
height=float(input('%s身高（m）:'%a))
weight=float(input('%s体重（Kg）:'%a))

bmi = weight / (height * height)

if bmi <= 18.4:
	print('过轻,BMI值：%.2f' %bmi)
elif bmi < 23.9:
	print('正常,BMI值：%.2f' %bmi)
elif bmi < 27.9:
	print('过重,BMI值：%.2f' %bmi)
elif bmi < 32:
	print('肥胖,BMI值：%.2f' %bmi)
else:
	print('严重肥胖')

