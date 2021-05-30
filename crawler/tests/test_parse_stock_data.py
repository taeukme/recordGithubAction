from crawler.parse_stock_data import parse_html, map_daily_price
import os

def test_parse_html():
    script_dir = os.path.dirname(__file__)
    file_path = os.path.join(script_dir, 'sample_files/sample_parse_html.html')

    with open(file_path, 'r') as file:
        contents = file.read().replace('\n', '')

        stock_data = parse_html(contents)

        expected_data = {'일별시세': [{'날짜': '2019.10.23', '종가': 123, '전일비': 20, '거래량': 300}],
                         '기본정보': [{'이름': '제주코딩베이스캠프', '시가총액': '1조 2,000',
                                   '시가총액순위': '1', '상장주식수': '5,969', '배당수익률': '2.42%',
                                   '매출': '1,209원', '비용': '12,235원', '순익': '300원'}]}

        assert stock_data == expected_data

def test_map_daily_price():
    날짜 = ['2021.01.01', '2021.01.02']
    종가 = [123, 456]
    전일비 = [30, 45]
    거래량 = [40, 50]

    expected_daily_price = [{'날짜': '2021.01.01', '종가': 123, '전일비': 30, '거래량': 40},
                            {'날짜': '2021.01.02', '종가': 456, '전일비': 45, '거래량': 50}]

    daily_price = map_daily_price(날짜, 종가, 전일비, 거래량)

    assert expected_daily_price == daily_price

