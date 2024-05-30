from scraper import get_data
def test_get_data():
    url = 'https://quotes.toscrape.com/'
    data = get_data(url)
    assert data['title'] == 'Quotes to Scrape'
    assert data['first_quote'] == '“The world as we have created it is a process of our thinking. ' \
                                  'It cannot be changed without changing our thinking.”'