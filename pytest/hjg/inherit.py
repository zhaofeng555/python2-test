#!/usr/bin/python

class SchoolMember:
	def __init__(self, name, age):
		self.name=name
		self.age=age
		print 'member: %s' % self.name
	def tell(self):
		print 'name: %s age: %s' % (self.name, self.age)

class Teacher(SchoolMember):
	def __init__(self, name, age, salary):
		SchoolMember.__init__(self, name, age)
		self.salary=salary
		print 'teacher: %s' % self.name

	def tell(self):
		SchoolMember.tell(self)
		print 'salary: %d' % self.salary

class Student(SchoolMember):
	def __init__(self, name, age, marks):
		SchoolMember.__init__(self, name, age)
		self.marks=marks
		print 'student: %s' % self.name

	def tell(self):
		SchoolMember.tell(self)
		print 'marks: %d' % self.marks

t=Teacher('Mrs. shr', 40, 30000)
s=Student('swar', 22, 75)

print '----------\n------------'

members=[t, s]
for member in members:
	member.tell()


