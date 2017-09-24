import requests

sitemap = requests.get('http://dveribelorussii.com.ua/ua/sitemap.xml')
with open('response_sitemap.xml', 'wb') as response: #указать путь к файлу xml
    response.write(sitemap.content)

message = 'Attention! The file was modified!'

with open('sitemap_origin.xml') as f1, open('response_sitemap.xml') as f2:
    for x, y in zip(f1, f2):
        if x != y:
            print(message)
            break