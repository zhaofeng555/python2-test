#!/usr/bin/python

def func(a, b=5, c=10):
	print 'a is ', a, 'and b is ', b, ' and c is ', c

func(2, 7)
func(23, c=24)
func(c=50, a=100)
