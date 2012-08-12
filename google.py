#!/usr/bin/python 

from bs4 import BeautifulSoup
import urllib, requests, sys

def google(query, max_results, urloptions = None):
    url = "https://www.google.com/search?q=" + urllib.quote(query)
    if urloptions is not None:
        for opt in urloptions.keys():
            url += "&%s=%s" % (opt, urloptions[opt])

    output = []
    count = 10
    
    while count <= max_results:
        count += 10
        url += "&start=" + str(count)
        soup = BeautifulSoup(requests.get(url).content)
        for link in soup('a'):
            if "/url?q=" in link['href']:
                output.append(str(link['href'].split('&')[0][7:]))

    return output
        
if len(sys.argv) < 2:
    sys.exit("Usage is (python) google 'query' [max_results [urloptions]]\n")
else:
    try:
        max_results = int(sys.argv[2])
    except:
        max_results = 10
    try:
        urloptions = sys.argv[3]
    except:
        urloptions = None
    print  "\n".join(google(sys.argv[1], max_results, urloptions))

