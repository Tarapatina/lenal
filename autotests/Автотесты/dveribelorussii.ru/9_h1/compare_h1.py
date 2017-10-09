import requests
from bs4 import BeautifulSoup

def main():

    with open('21.txt', 'r') as list_urls:
        for url in list_urls.readlines():
            resp = requests.get(url).content
            soup = BeautifulSoup(resp, 'html.parser')
            div = soup.find_all("img", {"class":"img-responsive"})

            wrong_list = []
            for el in div:
                title = (el.get('title'))
                alt = (el.get('alt'))
                if title != alt:
                    wrong_list.append(url)
                    print(url)
                    print(el)
                else: print('условие выполняется')


if __name__ == '__main__':
    main()



















if __name__ == '__main__':
    main()