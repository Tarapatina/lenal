import requests

robots = requests.get('https://dveribelorussii.ru/robots.txt')
with open('response_robots.txt', 'wb') as response:
    response.write(robots.content)

message = 'Attention! The file https://dveribelorussii.ru/robots.txt was modified!'

with open('robots_origin.txt') as f1, open('response_robots.txt') as f2:
    for x, y in zip(f1, f2):
        if x != y:
            print(message)
            break