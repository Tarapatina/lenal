import requests
from bs4 import BeautifulSoup


def main():
    with open('list_new.txt', 'r') as list_urls:
        for url in list_urls.readlines():
            resp = requests.get(url.replace('\n', '')).content
            soup = BeautifulSoup(resp, 'html.parser')
            lang = soup.find_all("link", {"rel":"alternate"})[:1]

            wrong_list = []
            for el in lang:
                el = (el.get('href'))
                if el is None in resp:
                    wrong_list.append(el)
                    print(wrong_list)
                else: print('условие выполняется')


if __name__ == '__main__':
    main()