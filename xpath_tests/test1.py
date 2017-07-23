import requests
from lxml import html

pageContent=requests.get(
    'https://en.wikipedia.org/wiki/List_of_Olympic_medalists_in_judo'
)
tree = html.fromstring(pageContent.content)