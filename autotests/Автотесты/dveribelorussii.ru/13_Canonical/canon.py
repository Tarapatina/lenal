import requests
from bs4 import BeautifulSoup


def main():
    with open('list_new.txt', 'r') as list_urls: #open('cano.txt', 'w') as cano_file:
        for url in list_urls.readlines():
            resp = requests.get(url.replace('\n', '')).content
            soup = BeautifulSoup(resp, 'html.parser')

            wrong_list = []
            canon = soup.find_all("link", {"rel":"canonical"})
            for el in canon:
                el = (el.get('href'))
                print('условие выполняется')
                if el is None:
                    wrong_list.append(url)
                    print(wrong_list)







if __name__ == '__main__':
    main()