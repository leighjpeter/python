#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import random
from retrying import retry

@retry
def do_something_unreliable():
	if random.randint(0, 10) > 1:
		raise IOError("Broken sauce, everything is hosed!!!111one")
	else:
		return "Awesome sauce!"

print (do_something_unreliable())



@retry(stop_max_delay=10000)
def stop_after_10_s():
	return "Stopping after 10 seconds"
print(1)
print (stop_after_10_s())


@retry(wait_fixed=2000)
def wait_2_s():
	return "Wait 2 second between retries"
print (wait_2_s())



def retry_if_result_none(result):
	"""Return True if we should retry (in this case when result is None), False otherwise"""
	return False

@retry(retry_on_result=retry_if_result_none)
def might_return_none():
	print ("Retry forever ignoring Exceptions with no wait if return value is None")

might_return_none()