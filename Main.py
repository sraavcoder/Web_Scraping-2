from bs4 import BeautifulSoup
import requests
import pandas as pd

START_URL = 'https://en.wikipedia.org/wiki/List_of_brown_dwarfs'

page = requests.get(START_URL)
soup = BeautifulSoup(page.text, 'html.parser')

table = soup.select('table')[4]
table_rows = table.find_all('tr')
Scraped_Data = []

for tr in table_rows:
    td = tr.find_all('td')
    row = [tag.text.rstrip() for tag in td]
    Scraped_Data.append(row)

del Scraped_Data[0]

df = pd.DataFrame(list(Scraped_Data), columns=[
    'Brown_Dwarf', 'Constellation', 'Right_Ascension', 'Declination', 'App_mag', 'Distance', 'Spectral_Type', 'Mass', 'Radius', 'Discovery_year'])

df.to_csv('Final.csv')
