import requests
from bs4 import BeautifulSoup

# send a GET request to the website
url = 'https://scholar.google.com/citations?view_op=view_org&hl=pt-BR&org=2925224885404296289&after_author=bXGLAK3___8J&astart=80'
response = requests.get(url)

# parse the HTML content of the page with BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# find all links on the page
links = soup.find_all('a')

# print the href attribute of each link
for link in links:
    print(link.get('href'))

with open("link.txt","a") as file:
        file.write(f'{link}\n')