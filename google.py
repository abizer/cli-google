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
    
    while count <= max_results - 10:
        url += "&start=" + str(count)
        count += 10
        soup = BeautifulSoup(requests.get(url).content)
        for link in soup('a'):
            if "/url?q=" in link['href']:
                if opts is not None:
                    if opts == "links":
                        output.append(str(link['href'].split('&')[0][7:]))
                        print str(link['href'].split('&')[0][7:])
                    elif opts == "names":
                        try:
                            output.append(str(link.text))
                            print str(link.text)
                        except:
                            output.append("\t ---- Name Contains Illegal Unicode Characters!")
                            print "\t ---- Name contains illegal Unicode Characters!"
                    elif opts == "descs":
                        try:
                            output.append(str(unicode((link.find_next('div').find('span', 'st').text)))
                            print str(unicode(link.find_next('div').find('span', 'st').text))
                        except:
                            output.append("\t ---- Description Contains Illegal Unicode")
                            print "\t ---- Description contins illegal Unicode."
                    else:
                        sys.exit("\tUnrecognized value '%s' for paramater opts! Recognized Parameters: names | links | descs" % opts)
                        break
                else:
                    output.append(str(link['href'].split('&')[0][7:]))
                    print str(link['href'].split('&')[0][7:])

    return output


print ""
    
if len(sys.argv) < 2:
    sys.exit("\tUsage is (python) google 'query' [options (names || descs || links)[max_results [urloptions]]]\n")
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
        urloptions = dict(sys.argv[4])
    except:
        urloptions = None
        
    results = google(sys.argv[1], opts, max_results, urloptions)

   # print "\n".join(results)

