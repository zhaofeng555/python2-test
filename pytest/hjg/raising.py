#!/usr/bin/python

class ShortInputException(Exception):
	def __init__(self, length, atleast):
		Exception.__init__(self)
		self.length=length
		self.atleast=atleast

try:
	s=raw_input('enter something-->')
	if len(s) < 3:
		raise ShortInputException(len(s), 3)
except EOFError:
	print '\nwhy?'
except ShortInputException, x:
	print 'shortinputexception: len=%d, least=%d' % (x.length, x.atleast)
else:
	print 'no exception was raised'
