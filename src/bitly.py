'''
Created on Aug 6, 2013
http://www.pythonforbeginners.com/code-snippets-source-code/bitly-shortener-with-python/
@author: mlecce
'''
#!/usr/bin/env python
 
# Import the modules
 
import bitly_api
 
def shorten(url):
    ACCESS_TOKEN = "9b6fe79fe1ee281ae5e7ec5af6d148315211e047"
    c = bitly_api.Connection(None, None, ACCESS_TOKEN, False)
    return c.shorten(url)