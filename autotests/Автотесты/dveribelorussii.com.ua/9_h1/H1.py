import requests
from bs4 import BeautifulSoup


def main():
    with open('list_new.txt', 'r') as list_urls, open('h1.txt', 'w') as h1:

        for url in list_urls.readlines():
            resp = requests.get(url.replace('\n', '')).content
            soup = BeautifulSoup(resp,'html.parser')

            for h11 in soup.find_all('h1', class_ = 'edit-title-cell__heading catal-heading'):
                h1.write(str(h11.text)+'\n')
                print(str(h11.text))

if __name__ == '__main__':
    main()