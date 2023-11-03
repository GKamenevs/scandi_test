import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://bulbapedia.bulbagarden.net/wiki/List_of_Pok%C3%A9mon_by_National_Pok%C3%A9dex_number'
r = requests.get(url)

url_part = 'https://bulbapedia.bulbagarden.net'

urls = pd.DataFrame(columns=['Index', 'Url'])

soup = BeautifulSoup(r.content, 'lxml')
tables = soup.find_all('table', class_='roundy')

for table in tables:
    rows = table.find_all('tr')[1:]

    for row in rows:
        link = row.find('a')  # Get the first anchor tag in the row
        if link and 'href' in link.attrs:  # Check if 'href' attribute exists
            href = link['href']  # Extract the value of the 'href' attribute
            full_url = url_part + href  # Combine with base URL if needed
            urls = urls._append({'Index': len(urls), 'Url': full_url}, ignore_index=True)

urls.to_csv('urls.csv', index=False)


