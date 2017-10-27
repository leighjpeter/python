#!/usr/bin/env python3
# -*- coding: utf-8 -*-
s1 = 75
s2 = 81
r = (s2 - s1) / s1 * 100
print('提升率：%.2f%%'%r)

s = 'Python-中文'
print(s)
b =s.encode('utf-8')
print(b)
print(b.decode('utf-8'))
print(s.replace('P','p'))

a=input('请输入录入成绩的名字:')
s1=(input('%s,前年的成绩:'%a))
s2=(input('%s,今年的成绩:'%a))
if s1 > s2:
    r=(s1-s2)/s1*100
    print('%s,成绩降低百分点=%d%%' % (a,r))
else:
    r=(s2-s1)/s2*100
    print('%s,成绩提升百分点=%d%%' % (a,r))