#!/usr/bin/python

poem='''\
programing is fun
when the work is done
if you wanna make your work also fun:
	use python !
'''

f=file('poem.txt', 'w') #w r a
f.write(poem)
f.close()

f=file("poem.txt")
while True:
	line=f.readline()
	if len(line) == 0:
		break
	print line,
f.close()





