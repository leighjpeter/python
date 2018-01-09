#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import time

sourceList = ['/Users/jessica/Wsmall/python/request_read.txt','/Users/jessica/Wsmall/python/request_read.txt']
target_dir = '/Users/jessica/Wsmall/backup'

today = target_dir + time.strftime('%Y%m%d')
now = time.strftime('%H%M%S')

comment = input('Enter a comment->')
if len(comment) == 0:
	target = today + os.sep + now + '.zip'
else:
	target = today + os.sep + now + '_'+\
		comment.replace(' ','_') + '.zip'

if not os.path.exists(today):
	os.mkdir(today)
	print('Successfully created directory %s' %today)


zip_command = "zip -qr '%s' %s " % (target, ' '.join(sourceList))
# tar_command = 'tar -cvzf %s %s' % (target, ' '.join(sourceList))

if os.system(zip_command) == 0 :
	print('Successfully backup to %s' %target)
else:
	print("Backup Failed")