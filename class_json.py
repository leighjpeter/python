#!/usr/bin/env python3
# -*- coding: utf-8 -*-
class cls_from_dict(object):
	pass

class cls_not_from_dict():
	pass

def cls2dict(obj):
	return obj.__dict__

cls_a = cls_from_dict()
cls_b = cls_not_from_dict()

cls_a.name = 'name_a'
cls_b.name = 'name_b'

print(cls_a.__dict__)
print(cls_b.__dict__)

print(dir(cls_a))