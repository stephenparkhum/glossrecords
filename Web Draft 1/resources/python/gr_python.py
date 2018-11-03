#Import libraries 
from requests import get
from bs4 import BeautifulSoup
import csv
from datetime import datetime

url = 'https://glossolaliarecords.bandcamp.com/'

response = get(url)
print(response.text[:500])

soup = BeautifulSoup(response.text, 'html.parser')

album_names = soup.find('p', attrs={'class': 'title'})
band_names = soup.find('span', attrs={'class' : 'artist-override'})

albums = album_names.text.strip()
bands = band_names.text.strip()

albums = " ".join(albums.split())

print(albums) 
print(bands)
