import requests

sitemap = requests.get('http://dveri-ua.lenal.work/sitemap_images.xml')
with open('response_sitemap_images.xml', 'wb') as response: #указать путь к файлу xml
    response.write(sitemap.content)

message = 'Attention! The file http://dveri-ua.lenal.work/sitemap_images.xml was modified!'

with open('sitemap_images_origin.xml') as f1, open('response_sitemap_images.xml') as f2:
    for x, y in zip(f1, f2):
        if x != y:
            print(message)
        else: print ('ok')
