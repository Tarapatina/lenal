import requests

sitemap = requests.get('https://dveribelorussii.com.ua/sitemap_filters.xml')
with open('response_sitemap_filters.xml', 'wb') as response: #указать путь к файлу xml
    response.write(sitemap.content)

message = 'Attention! The file https://dveribelorussii.com.ua/sitemap_filters.xml was modified!'

with open('sitemap_filters_origin.xml') as f1, open('response_sitemap_filters.xml') as f2:
    for x, y in zip(f1, f2):
        if x != y:
            print(message)
            break