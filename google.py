#! /usr/bin/env python 

from bs4 import BeautifulSoup
import urllib, requests, sys

def google(query, urloptions=None):
    url = "https://www.google.com/search?q=" + urllib.quote(query)
    if urloptions is not None:
        for opt in urloptions.keys():
            url += "&%s=%s" % (opt, urloptions[opt])
    soup = BeautifulSoup(requests.get(url).content)
    output = []
    for link in soup('a'):
        if "/url?q=" in link['href']:
            output.append(str(link['href'].split('&')[0][7:]))

    return output
        
if len(sys.argv) < 2:
    sys.exit("Usage is (python) google 'query'\n")
else:
    print  "\n".join(google(sys.argv[1], {"start":10}))#! /usr/bin/env python 

from bs4 import BeautifulSoup
import urllib, requests, sys

def google(query, urloptions=None):
    url = "https://www.google.com/search?q=" + urllib.quote(query)
    if urloptions is not None:
        for opt in urloptions.keys():
            url += "&%s=%s" % (opt, urloptions[opt])
    soup = BeautifulSoup(requests.get(url).content)
    output = []
    for link in soup('a'):
        if "/url?q=" in link['href']:
            output.append(str(link['href'].split('&')[0][7:]))

    return output
        
if len(sys.argv) < 2:
    sys.exit("Usage is (python) google 'query'\n")
else:
    print  "\n".join(google(sys.argv[1], {"start":10}))
