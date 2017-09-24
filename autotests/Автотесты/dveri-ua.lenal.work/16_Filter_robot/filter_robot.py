import requests
from bs4 import BeautifulSoup


def main():
    with open('filter.txt', 'r') as list_urls: #open('lang.txt', 'w') as lang:
        for url in list_urls.readlines():
            resp = requests.get(url).content
            soup = BeautifulSoup(resp, 'html.parser')
            robot = soup.find_all("meta", {"name":"robots"})



            el_list = []
            for el in robot:
                print(el)
                if el is None:
                    print('wrong')
                    el_list.append(url)
            print(el_list)







if __name__ == '__main__':
    main()