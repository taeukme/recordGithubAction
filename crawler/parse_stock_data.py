from bs4 import BeautifulSoup

def parse_html(html):
    soup = BeautifulSoup(html, 'html.parser')

    제코베연구원_컨테이너 = soup.select('.main')[2]
    제코베연구원_일별시세 = 제코베연구원_컨테이너.select('tbody > tr')[1:]

    시가총액 = soup.select('#_market_sum')[0].text
    시가총액순위 = soup.select('#_market_sum')[1].text
    상장주식수 = soup.select('#_market_sum')[2].text
    주가_추가정보 = soup.select('tr > td')
    배당수익률 = 주가_추가정보[5].text.strip()
    매출 = 주가_추가정보[6].text
    비용 = 주가_추가정보[7].text
    순익 = 주가_추가정보[8].text

    날짜 = []
    종가 = []
    전일비 = []
    거래량 = []

    for i in 제코베연구원_일별시세:
        날짜.append(i.select('td')[0].text)
        종가.append(int(i.select('td')[1].text.replace(',', '')))
        전일비.append(int(i.select('td')[2].text.replace(',', '')))
        거래량.append(int(i.select('td')[6].text.replace(',', '')))

    daily_price = map_daily_price(날짜, 종가, 전일비, 거래량)

    stock_data = {
        '일별시세': daily_price,
        '기본정보': [{
            "이름" : "제주코딩베이스캠프",
            "시가총액" : 시가총액,
            "시가총액순위" : 시가총액순위,
            "상장주식수" : 상장주식수,
            "배당수익률" : 배당수익률,
            "매출" : 매출,
            "비용" : 비용,
            "순익" : 순익
        }]
    }

    return stock_data

def map_daily_price(날짜, 종가, 전일비, 거래량):
    daily_price = []

    for i in range(len(날짜)):
        daily_price.append({
            '날짜':날짜[i],
            '종가':종가[i],
            '전일비':전일비[i],
            '거래량':거래량[i],
            })

    return daily_price
