#!/usr/bin/python

name='hello world'
if name.startswith('hel'):
	print 'yes, the string starts with "hel"'
if 'o' in name:
	print 'yes, it contains "o"'

delimiter="hehe"
mylist=['aa', 'bb', 'cc', 'dd']
print delimiter.join(mylist)
