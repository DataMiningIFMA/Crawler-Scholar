import requests
import re 

url = "https://scholar.google.com/citations?view_op=view_org&org=2925224885404296289&hl=pt-BR&oi=io"
check = []

r = requests.get(url, headers = {'User-agent': 'your bot 0.1'})
html = r.text.encode("utf8")
search = re.findall(r'<a href=[\'"?](https[://\w\-._]+)',html.decode("utf8"))

for link in search:
   if link not in check:
      check.append(link)
      
      with open("link.txt","a") as file:
        file.write(f'{link}\n')