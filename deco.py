# -*- coding: utf-8 -*-

from functools import wraps
def debug(msg=''):
	def mydecorator(func):
		@wraps(func)
		def wrapper(*args, **kwargs):
			print(msg)
			return func(*args, **kwargs)
		return wrapper
	return mydecorator

@debug('deco1')
def deco1(func):
	def wrapper(*args, **kwargs):
		return func(*args, **kwargs)
	return wrapper

@debug('deco2')
def deco2(func):
	def wrapper(*args, **kwargs):
		return func(*args, **kwargs)
	return wrapper 


@deco2
@deco1
def add(x, y):
	return x + y

print(add(2, 3))
