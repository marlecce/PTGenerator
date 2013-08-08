'''
Created on Aug 6, 2013
http://www.pythonforbeginners.com/code-snippets-source-code/bitly-shortener-with-python/
@author: mlecce
'''
#!/usr/bin/env python
 
# Import the modules
 
import bitly_api
 
def shorten(url):
    ACCESS_TOKEN = "your_access_token"
    c = bitly_api.Connection(None, None, ACCESS_TOKEN, False)
    return c.shorten(url)