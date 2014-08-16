#!/usr/bin/python

class Person:
	'''represents a person.'''
	population=0

	def __init__(self, name):
		self.name=name
		print 'name=%s' % self.name

		Person.population += 1

	def __del__(self):
		'''dying'''
		print 'bye'

		Person.population -= 1

		if Person.population == 0:
			print 'I am the last one'
		else:
			print 'there are %d' % Person.population

	def sayHi(self):
		print 'hi, my name is %s.' % self.name

	def howMany(self):
		print 'persons %d here.' % Person.population		

p=Person('hello')
p.sayHi()
p.howMany()

k=Person("world")
k.sayHi()
k.howMany()

#p.sayHi()
#p.howMany()
