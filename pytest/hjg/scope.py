#!/usr/bin/python

def line_conf():
    	def line(x):
            	return 2*x+1
        #print(line(5))
	return line

line_conf()
#print(line(3))
myline=line_conf()
print(myline(5))
