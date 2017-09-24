import requests
from bs4 import BeautifulSoup

def main():
    with open('11.txt','r') as list_urls, open('description.txt','w', encoding='utf-8') as desc_file:
        for url in list_urls.readlines():
            resp = requests.get(url.replace('\n', '')).content
            soup = BeautifulSoup(resp, 'html.parser')
            desc = soup.find_all("class", {"class":"shawall"})


            for el in desc:
                el = (el.get('content'))
                desc_file.write(el+'\n')
                print(el)