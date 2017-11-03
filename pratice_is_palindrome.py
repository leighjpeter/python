#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def is_palindrome(n):
	a = str(n)
	b = str(n)[::-1]
	if a == b:
		return True
	else:
		return False


def is_palindrome(n):
    new = list(str(n))
    new.reverse()
    # ''.join(new)  list2str
    return n == int(''.join(new))

output = filter(is_palindrome, range(1, 1000))
print(list(output))