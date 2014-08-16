#!/usr/bin/python

ab={
	'java':'java.com',
	'c':'c.com',
	'python':'python.com'
}

print "java' s address is %s" % ab['java']

print ab

ab['delphi']='delphi.com'

del ab['c']

print len(ab)

for name, address in ab.items():
	print 'contact %s at %s' % (name, address)

if 'python' in ab:
	print "python's address is %s" % ab['python']
