import requests
from bs4 import BeautifulSoup


def main():
    with open('filter.txt', 'r') as list_urls:

        for url in list_urls.readlines():
            resp = requests.get(url.replace('\n', '')).content
            soup = BeautifulSoup(resp, 'html.parser')
            robot = soup.find_all("link", {"rel":"canonical"})

            el_list = []
            for el in robot:
                el = (el.get('href'))
                el_list.append(el)
                print(el_list)









if __name__ == '__main__':
    main()