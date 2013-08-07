'''
Created on Aug 6, 2013
source: http://segfault.in/2010/10/shorten-urls-using-python-and-bit-ly/
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