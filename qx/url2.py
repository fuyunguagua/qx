# encoding=utf-8
import base64
import email
import email.message
import mimetypes
import os
import quopri
import sys
import requests
#import urllib2
#from HTMLParser import HTMLParser
#from urlparse import urlparse
import chardet
'''

class MHTHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.urls = []
    def handle_starttag(self, tag, attrs):
        if not tag in ['link']:  # , 'script'
            return
        attrs = dict(attrs)
        a = attrs.get('src')
        if a and a.find('google') == -1:
            self.urls.append((a, attrs.get('type', 'text/javascript')))
        elif attrs.get('rel') == 'stylesheet':
            self.urls.append(
                (attrs.get('href'), attrs.get('type', 'text/css')))
class URL2MHT(object):
    def __init__(self, url):
        uparse = urlparse(url)
        self.domain = uparse.scheme + "://" + uparse.netloc
        self.url = url
        self.header = {
            'User-Agent': "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:39.0) Gecko/20100101 Firefox/39.0"}
    def _head(self):
        a = email.message.Message()
        a["MIME-Version"] = "1.0"
        a["X-UnMHT-Save-State"] = "Current-State"
        a.add_header("Content-Type",
                     "multipart/related",
                     type="text/html")
        return a
    def mht(self):
        content = urllib2.urlopen(
            urllib2.Request(self.url, None, self.header)).read()
        pmht = MHTHTMLParser()
        pmht.feed(content)
        pmht.close()
        head = self._head()
        head.attach(self._add(self.url, utype='text/html'))
        for url, utype in pmht.urls:
            head.attach(self._add(url, utype))
        return head
    def _add(self, url, utype=None):
        m = email.message.Message()
        content = None
        local_url = None
        if not urlparse(url).netloc:
            local_url = self.domain + url
        else:
            local_url = url
        ctn = None
        ecd = None
        content = urllib2.urlopen(
            urllib2.Request(local_url, None, self.header)).read()
        if utype and utype.startswith("text/"):
            ecd = "quoted-printable"
            ctn = quopri.encodestring(content)
        else:
            ecd = "base64"
            ctn = base64.b64encode(content)
        m["Content-Transfer-Encoding"] = ecd
        m["Content-Location"] = local_url
        m["Content-Type"] = utype
        m.set_payload(ctn)
        return m
# url = 'http://www.cnblogs.com/weixliu/p/3554868.html'
url = 'http://mp.weixin.qq.com/s?__biz=MzIzNTM5Mzg0Mg==&amp;mid=2247485046&amp;idx=1&amp;sn=002cb01662f874f00ee62992e4f65bd2&amp;chksm=e8e6802bdf91093df74f1419dcb17e52d60dda84464c9cdd3689eca008bded543ffd3fe21591&amp;scene=27#wechat_redirect'
a = URL2MHT(url).mht().as_string(unixfrom=False)

import codecs
fh = codecs.open("hello.mht", mode="wb", encoding="utf-8")
fh.write(a)
fh.close()

'''
'''
x = open('hello.mht').read()
print type(x)
print chardet.detect(x)
x = x.decode('utf-8')
print type(x)
print chardet.detect(x)'''
