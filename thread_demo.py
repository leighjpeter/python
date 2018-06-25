#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import threading
#非阻塞
class ThreadJob(threading.Thread):
	"""docstring for ThreadJob"""
	def __init__(self, callback, event, interval):
		'''runs the callback function after interval seconds

        :param callback:  callback function to invoke
        :param event: external event for controlling the update operation
        :param interval: time in seconds after which are required to fire the callback
        :type callback: function
        :type interval: int
        '''
		super(ThreadJob, self).__init__()
		self.callback = callback
		self.event = event
		self.interval = interval

	def run(self):
		while not self.event.wait(self.interval):
			self.callback()


event = threading.Event()

def foo():
	print('LOL')

k = ThreadJob(foo,event,2)
k.start()

print('non-blocking')