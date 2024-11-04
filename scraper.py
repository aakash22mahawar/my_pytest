import requests
from bs4 import BeautifulSoup


def get_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    title = soup.title.text
    quote = soup.select_one('span.text').text
    return {'title': title, 'first_quote': quote}
