import requests

robots = requests.get('http://dveri-ua.lenal.work/robots.txt')
with open('response_robots.txt', 'wb') as response:
    response.write(robots.content)

message = 'Attention! The file http://dveri-ua.lenal.work/robots.txt was modified!'

with open('robots_origin.txt') as f1, open('response_robots.txt') as f2:
    for x, y in zip(f1, f2):
        if x != y:
            print(message)
            break