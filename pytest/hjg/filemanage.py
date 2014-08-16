#!/usr/bin/python

f=open("poem.txt", "w")
print(f.closed)
f.write("hello world")
f.close()
print(f.closed)

print '---------------'

with open("poem.txt","w") as f:
	print(f.closed)
	f.write("hello world!")
print(f.closed)
