#!/usr/bin/python

print 'abc'+'xyz'
print 'abc'.__add__('xyz')

print (1.8).__mul__(2.0)
print len([1,2,3])
print [1,2,3].__len__()
li=[1,2,3,4,4,5,6]
print(li.__getitem__(3))
