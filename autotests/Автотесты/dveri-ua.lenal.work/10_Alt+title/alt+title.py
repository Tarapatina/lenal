import requests
from bs4 import BeautifulSoup

def main():

    with open('list_new.txt', 'r') as list_urls:
        for url in list_urls.readlines():
            resp = requests.get(url).content
            soup = BeautifulSoup(resp, 'html.parser')
            div = soup.find_all("img", {"class":"img-responsive"})

            wrong_list = []
            for el in div:
                alt = (el.get('alt'))
                title = (el.get('title'))



                if title != alt:
                    wrong_list.append(url)
                    print(url)
                    print(el)
                #else: print('условие выполняется')


if __name__ == '__main__':
    main()





