import requests
from bs4 import BeautifulSoup
import csv
import json 

data = requests.get('https://glossolaliarecords.bandcamp.com/')

soup = BeautifulSoup(data.text, 'html-parser')

soup.find_all('div')
print(soup)

# Pull text from all instances of <a> tag within BodyText div
#artist_title = columns.find('li')
#artists = artist_title.find('span', class_='artist-override')

#band_name_list_items = columns.find_all('span', class_='artist-override')
#columns_items = columns.find_all('p', class_='title')

# print(band_name_list_items)
#for p in artist_title.find_all('p', { "class" : "title" }):
        #print(p)
        #title = p.text.strip()
        #artist = p.find('span').text.strip()
       # title = title.replace(artist, "").strip()
        #print(artist, title)
        #f.writerow([artist, title])

#for p in artists.find('p'):
 #   
  #      print(p)


# for band_name in band_name_list_items:
  #   band = band_name.text
#     band = " ".join(band_name.text.split())
# 
  #   for title_name in title_name_list_items:
  #       title = title_name.text
   #      if band in band_name_list_items: 
    #             band_strip = band.strip(band_name_list_items)
      #           print(band)
       #          strings = title.split(" ")
      #           title = " ".join(title_name.text.split())
       #  print(title)
    #f.writerow([band, title])
