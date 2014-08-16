#!/usr/bin/python
s=raw_input("enter something: ")
print s	, 'Done'

birth = raw_input('birth: ')
if birth < 2000:
	print '<00'
else:
	print '>00'

print birth, ' < 2000 ', birth<2000

print '--------to int------------'

print birth, ' < 2000 ', int(birth)<2000

