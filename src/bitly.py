'''
Created on Aug 6, 2013
source: http://segfault.in/2010/10/shorten-urls-using-python-and-bit-ly/
@author: mlecce
'''
#!/usr/bin/env python
 
# Import the modules
 
import bitly_api
import sys
 
def shorten(url):
    API_USER = ""
    API_KEY = ""
    b = bitly_api.BitLy(API_USER, API_KEY)
    # Define how to use the program
    if len(sys.argv) != 2:
        sys.exit(0)
    longurl = sys.argv[1]
    return b.shorten(longUrl=longurl)