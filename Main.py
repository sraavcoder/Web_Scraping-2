from bs4 import BeautifulSoup
import requests
import pandas as pd

START_URL = 'https://en.wikipedia.org/wiki/List_of_brown_dwarfs'

page = requests.get(START_URL)
soup = BeautifulSoup(page.text, 'html.parser')

table = soup.select('table')[4]
table_rows = table.find_all('tr')
temp_list = []

for tr in table_rows:
    td = tr.find_all('td')
    row = [tag.text.rstrip() for tag in td]
    temp_list.append(row)

Brown_Dwarf_names = []
Cons = []
Distance = []
Mass = []
Radius = []

for i in range(1, len(temp_list)):
    Brown_Dwarf_names.append(temp_list[i][0])
    Cons.append(temp_list[i][1])
    Distance.append(temp_list[i][5])
    Mass.append(temp_list[i][7])
    Radius.append(temp_list[i][8])

df = pd.DataFrame(list(zip(Brown_Dwarf_names, Cons, Distance, Mass, Radius)), columns=[
    'Brown_Dwarf', 'Constellation', 'Distance', 'Mass', 'Radius'])

df.to_csv('Final.csv')
