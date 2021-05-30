from fetch_data import get_remote_data
from parse_stock_data import parse_html
from create_file import write_json

def main():
    print('Starting crawler...')
    url = 'http://paullab.synology.me/stock.html'
    html = get_remote_data(url)
    stock_data = parse_html(html)
    print(stock_data)

    write_json(stock_data['기본정보'], 'json/fetchtestbasicdata.json')
    write_json(stock_data['일별시세'], 'json/fetchtestdata.json')
    

if __name__ == '__main__':
    main()