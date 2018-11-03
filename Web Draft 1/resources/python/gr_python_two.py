import requests
from bs4 import BeautifulSoup
import csv


# Collect and parse first page
page = requests.get('https://glossolaliarecords.bandcamp.com/')
soup = BeautifulSoup(page.text, 'html.parser')

# Pull all text from the BodyText div
artist_name_list = soup.find(class_='leftMiddleColumns')

# Pull text from all instances of <a> tag within BodyText div
artist_name_list_items = artist_name_list.find_all(class_='title')

for artist_name in artist_name_list_items:
    names = artist_name.contents[0]
    print(names)
    

