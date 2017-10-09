import requests
from bs4 import BeautifulSoup


def main():
    with open('list_new.txt', 'r') as list_urls, open('lang.txt', 'w') as lang:
        for url in list_urls.readlines():
            resp = requests.get(url.replace('\n', '')).content
            soup = BeautifulSoup(resp, 'html.parser')


            lang = soup.find_all("link", {"rel":"alternate"})[:1]
            wrong_list = []
            for el in lang:
                el = (el.get('href'))
                if el is None in lang:
                    wrong_list.append(el)
                    print('wrong' + url)
                    print(wrong_list)

                else: print('ok')


if _name_ == '__main__':
    main()