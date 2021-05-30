from crawler.fetch_data import get_remote_data
from bs4 import BeautifulSoup

def test_get_remote_data():
    url = 'http://paullab.synology.me/stock.html'
    html = get_remote_data(url)

    soup = BeautifulSoup(html, 'html.parser')

    title = soup.find('title').string
    assert title == 'Document'

    stock_header = soup.select('#information > h2')[0].text
    assert stock_header == '(주)캣네생선'