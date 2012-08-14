#!/usr/bin/python 

from bs4 import BeautifulSoup
import urllib, requests, sys

def google(query, opts = None, max_results = None, urloptions = None):
    url = "https://www.google.com/search?q=" + urllib.quote(query)
    if urloptions is not None:
        for opt in urloptions.keys():
            url += "&%s=%s" % (opt, urloptions[opt])
    
    output = []
    count = 0
    
   # while count <= max_results:
    url += "&start=" + str(count)
    count += 10
    soup = BeautifulSoup(requests.get(url).content)
    for link in soup('a'):
        if "/url?q=" in link['href']:
            if opts is not None:
                if opts == "links":
                    output.append(str(link['href'].split('&')[0][7:]))
                elif opts == "names":
                    try:
                        output.append(str(link.text))
                    except:
                        output.append("Name Contains Illegal Unicode Characters!")
                elif opts == "descs":
                    try:
                        output.append(str(link.text))
                    except:
                        output.append("Description Contains Illegal Unicode")  
                else:
                    sys.exit("Unrecognized value '%s' for paramater opts! Recognized Parameters: names | links | descs" % opts)
            else:
                output.append(str(link['href'].split('&')[0][7:]))

    return (output, url)



    
if len(sys.argv) < 2:
    sys.exit("Usage is (python) google 'query' [options (names || descs || links)[max_results [urloptions]]]\n")
else:
    try:
        opts = sys.argv[2]
    except:
        opts = None
    try:
        max_results = int(sys.argv[3])
    except:
        max_results = 10
    try:
        urloptions = sys.argv[4]
    except:
        urloptions = None
        
    (results, url) = google(sys.argv[1], opts, max_results, urloptions)

    print "\n".join(results)

