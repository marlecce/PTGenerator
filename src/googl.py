'''
Created on Aug 6, 2013

@author: mlecce
'''
#!/usr/bin/python 

import json
import urllib
import urllib2


def shorten(url):
    gurl = 'http://goo.gl/api/url?url=%s' % urllib.quote(url)
    req = urllib2.Request(gurl, data='')
    req.add_header('User-Agent', 'toolbar')
    
    #set proxy
    proxy_support = urllib2.ProxyHandler({'http': 'http://proxy.reteunitaria.piemonte.it:3128'})
    opener = urllib2.build_opener(proxy_support)
    urllib2.install_opener(opener)
    
    results = json.load(urllib2.urlopen(req))
    return results['short_url']