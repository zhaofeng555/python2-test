import httplib



http=httplib.HTTPConnection('www.baidu.com', 80)
http.request('GET', '/index.php')

print http.getresponse().read()

http.close()