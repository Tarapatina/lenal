import requests
from bs4 import BeautifulSoup


def main():
    with open('filter.txt', 'r') as list_urls: #open('lang.txt', 'w') as lang:
        url_list = []
        for url in list_urls.readlines():
            resp = requests.get(url.replace('\n', '')).content
            soup = BeautifulSoup(resp, 'html.parser')
            robot = soup.find_all("link", {"rel":"canonical"})
            #url_list.append(url)
            #print(url_list)


            el_list = []
            for el in robot:
                el = (el.get('href'))
                el_list.append(el)
                print(el_list)



            #print(el_list)
        #print(url_list)

                # if el == url:
                #     print('w')
                #     #el_list.append(url)
                #     #print(el_list)
                # #else: print('ok')






if __name__ == '__main__':
    main()