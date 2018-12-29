#!/usr/bin/env python3
# -*- coding: utf-8 -*-

### 添加字典的方法
optons = {'code':'utf-8'}
base_headers = {
	'User-Agent' : 100,
	'Accept-Encoding' : 'gzip, deflate, sdch',
	'Accept-Language' : 'zh-Cn,zh;q=0.8'
}

headers=dict(base_headers, **optons)

print(headers)

base_headers.update(optons)

print(base_headers)


### 推导列表
print([x/2 for x in range(10) if x%2 == 0])
# [0.0, 1.0, 2.0, 3.0, 4.0]
print( [x+1 if x>=5 else x*10 for x in range(10)] )
# [0, 10, 20, 30, 40, 6, 7, 8, 9, 10]

### 碾平list
s = [1,[2,[3,4]],['a','b']]
res = []
def fun(s):
	for x in s:
		if isinstance(x,list):
			fun(x)
		else:
			res.append(x)
fun(s)
print(res)

flat = lambda L: sum(map(flat,L),[]) if isinstance(L,list) else [L]
print(flat(s))

# map
l3 = map(lambda x,y:(x**y,x+y),[1,2,3],[1,2])
for i in l3:
	print(i)

# better
nums = [str(n) for n in range(20)]
print(''.join(nums))
# best
nums = map(str,range(20))
print(''.join(nums))
