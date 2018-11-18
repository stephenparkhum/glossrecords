import requests
from bs4 import BeautifulSoup
import csv
import json 
from datetime import timedelta
import re
import os 

# Collect and parse first page

gr_bc = 'https://glossolaliarecords.bandcamp.com/'
page = requests.get(gr_bc)
soup = BeautifulSoup(page.text, 'html.parser')

# Pull all text from the BodyText div
columns = soup.find('div', { "class" : "leftMiddleColumns" })


# Create CSV
f = csv.writer(open('gr-artist-names.csv', 'w'))
f.writerow(['Band', 'Album', 'Release Date', 'BC-URL', 'Genre'])


# -- MAIN 'FOR LOOP' to scrape information -- 

for p_two in columns.find_all('p', { "class" : "title" }):
        title = p_two.text.strip()
        for p_three in p_two.find_all('span'):
                artist = p_two.find('span').text.strip()
                title = title.replace(artist, "").strip()
                if title == "": 
                        title = artist


        title_url = title.replace(' ', '-').replace('.', '')
        bc_url = gr_bc + "album/" + title_url.lower()
        bc_url_req = requests.get(bc_url)
        bc_url_soup = BeautifulSoup(bc_url_req.text, 'html.parser')
        
        #print(artist, title)
        
        #Create GR Dictionary of Artists/Titles
        
        
        grdict = {
                "artist": artist,
                "title": title,
                "bc-url": bc_url,
                "rel-date": " ",
                "genre": " ", 
                "rel-img": " " 

        }
        

        print(grdict)
        #Write info to CSV
        f.writerow([artist, title, grdict['rel-date'], bc_url, grdict['genre']])
        
        

# Release date scarpe 




