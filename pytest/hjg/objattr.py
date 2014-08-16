#!/usr/bin/python

class bird(object):
      	feather=True
	
class chicken(bird):
	fly=False
	def __init__(self, age):
		self.age=age

summer=chicken(2)


print(bird.__dict__)
print(chicken.__dict__)
print(summer.__dict__)

summer.__dict__['age']=3
print(summer.__dict__['age'])

summer.age=5
print(summer.age)
