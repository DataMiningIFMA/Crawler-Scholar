import requests
from bs4 import BeautifulSoup
import csv

def obter_texto(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/5336'}
    r = requests.get(url, headers=headers)
    html = r.text
    soup = BeautifulSoup(html, 'html.parser')
    texto = soup.get_text()
    return texto

def bia_csv(texto, nick):
    with open(nick, 'w', encoding='utf-8', newline='') as arquivo_csv:
        pao_csv = csv.writer(arquivo_csv)
        linhas = texto.split('\n')
        for linha in linhas:
            pao_csv.writerow([linha])


url = "./link.py"
texto_extraido = obter_texto(url)

nick_csv = "texto_extraido.csv"
bia_csv(texto_extraido, nick_csv)

print(f"Texto Extraído salvo em {nick_csv}")
