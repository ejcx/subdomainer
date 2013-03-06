import urllib2
import sys
import re
import time

'''
Created on Mar 2, 2013
@descr:  little script that finds subdomains of a domain specified
         as a command line argument
@author: Evan J Johnson
'''

def curldom(domain):
    foundsubdomains = []
    num = 1

    while True:
        d = urllib2.urlopen("http://www.bing.com/search?q=site%3A" + domain + "&first=" + str(num)).read()
        links =  d.split("<a href=")
        for i in links:
            if "."+domain in i:
                pagematches = i.split('"')
                possiblesubdomain = pagematches[1:2:][0].split("." + domain+ "/")[0]
                if possiblesubdomain not in foundsubdomains:
                    print possiblesubdomain
                    foundsubdomains.append(possiblesubdomain)
                    
        #don't go too fast, or bing will force you to pass a reverse turing test
        time.sleep(1)
        num+=10

    
if __name__ == '__main__':
    try:
        domain = sys.argv[1]
        curldom(domain)
    except IndexError:
        print "Usage:"
        print "\tpython subdomainer.py <domain>"
        print "Example:"
        print "\tpython subdomainer.py google.com"
        print "\tpython subdomainer.py example.com"
        
        
    
    
