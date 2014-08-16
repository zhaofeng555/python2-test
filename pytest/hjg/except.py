#!/usr/bin/python
import sys

try:
	s=raw_input('enter something --> ')
except EOFError:
	print '\nWhy did you do an EOF on me?'
	sys.exit()
except:
	print '\nsome error/exception occurred.'
print 'Done'
