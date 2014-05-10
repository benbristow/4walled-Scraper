from bs4 import BeautifulSoup
import requests
import os,sys
import urllib
import re

#EDIT BELOW THIS LINE

#Enter your search URL here (Remove the placeholder first). Get this from just searching like normal on 4walled.cc and copying the URL.
url = "http://4walled.cc/search.php?tags=&board=&width_aspect=&searchstyle=larger&sfw=0&search=search"
#Enter your download path here (This will download to a new folder, wallpapers, in the directory this script is ran from)
path = "wallpapers/"
#Pages of wallpapers to download (30 per page)
limit = 1

#DONT EDIT BELOW THIS LINE

resultsurl = url.replace("/search.php", "/results.php") + "&offset="
if not os.path.exists(path): os.makedirs(path)


for i in range(0, limit):
    offset = i * 30
    imagepageurl = resultsurl + str(offset)
    r = requests.get(imagepageurl)
    html = r.text
    
    soup = BeautifulSoup(html)    
    
    for tag in soup.find_all("img"):
        thumburl = tag['src']
        realurl = thumburl.replace("/thumb/", "/src/")
        
        try:
            r = requests.get(realurl)
            r.raise_for_status()            
        except:
            realurl = realurl.replace(".jpg" , ".png")
            
        filepath = path + realurl.split("/")[5]
        fr = requests.get(realurl)
        with open(filepath, "wb") as writer:
            writer.write(fr.content)
        fr.close()
        print "Downloading to " + filepath
