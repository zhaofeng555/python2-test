import urllib2

opener=urllib2.build_opener()
f=opener.open("http://www.baidu.com/index.php")
f.read()
f.close()