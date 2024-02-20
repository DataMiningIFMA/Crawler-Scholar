
import requests
from bs4 import BeautifulSoup
import urllib.parse

url = "desisto"

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/5336'}

r = requests.get(url, headers=headers)

soup = BeautifulSoup(r.text, 'html.parser') 
goku_links = set()

for link in soup.find_all('a', href=True):
    href = link['href']
    absolute_url = urllib.parse.urljoin(url, href)
    goku_links.add(absolute_url)

with open("link.txt", "a") as file:
    for link in goku_links:
        print(link)
        file.write(f'{link}\n')