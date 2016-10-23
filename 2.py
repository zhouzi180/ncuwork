from urllib.parse import urlencode
from urllib import request as urllib2
from http import cookiejar as cookielib

url = "http://222.204.3.49:8082/user/Index.aspx"
auth = {"username": "name", "password": "password"}
cookies = cookielib.CookieJar()
handler = urllib2.HTTPCookieProcessor(cookies)
opener = urllib2.build_opener(handler)
reponse = opener.open(url, urlencode(auth).encode("utf-8"))
for cookie in cookies:
    print (cookie)
