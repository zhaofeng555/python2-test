#!/usr/bin/python
import re
import urllib

def getHtml(url):
	page=urllib.urlopen(url)
	html=page.read()
	return html

def getImg(html):
	reg=r'src="(http.*?\.jpg)"'
	imgre=re.compile(reg)
	imglist=re.findall(imgre, html)
	x=0
	for imgurl in imglist:
		print x ,"->",  imgurl
		urllib.urlretrieve(imgurl, '%s.jpg' % x)
		x+=1
	return imglist

url="http://haha.sogou.com/248559/"
html = getHtml(url)
#print html
img = getImg(html)

#print img
