'''
Created on Aug 6, 2013
http://www.pythonforbeginners.com/code-snippets-source-code/bitly-shortener-with-python/
@author: mlecce
'''
#!/usr/bin/env python
 
# Import the modules
 
import bitly_api
 
def shorten(url):
    API_USER = ""
    API_KEY = ""
    b = bitly_api.BitLy(API_USER, API_KEY)
    return b.shorten(url)