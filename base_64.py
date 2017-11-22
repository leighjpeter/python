#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# base64
# 对二进制数据进行处理，每3个字节一组，一个字节byte=8bit,也就是3*8=24(bit),化为组，每组正好6bit。
# 得到4个数字作为索引，然后查表，获得相应的4个字符，就是编码后的字符串
# 所以，Base64编码会把3字节的二进制数据编码为4字节的文本数据，长度增加33%
# 如果要编码的二进制数据不是3的倍数，最后会剩下1个或2个字节怎么办？Base64用\x00字节在末尾补足后，再在编码的末尾加上1个或2个=号，表示补了多少字节，解码的时候，会自动去掉。
# 标准的base64编码之后会出现+和/,在URL中不能直接作为参数，所以有'urlsafe' 的base64 ,就是把+和/换成-和_

# 小结：
# Base64是一种任意二进制到文本字符串的编码方法，常用于在URL、Cookie、网页中传输少量二进制数据。
import base64

base64.b64encode(b'i\xb7\x1d\xfb\xef\xff') # b'abcd++//'

base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff') # b'abcd--__'

def safe_base64_decode(s):
	if isinstance(s,str):
		s = bytes(s,encoding='utf-8')
	c = len(s) % 4
	s = s+b'=' * c
	return base64.urlsafe_b64decode(s)

assert b'abcd' == safe_base64_decode(b'YWJjZA=='), safe_base64_decode('YWJjZA==')
assert b'abcd' == safe_base64_decode(b'YWJjZA'), safe_base64_decode('YWJjZA')
print('ok')