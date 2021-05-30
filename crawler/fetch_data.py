import requests

def get_remote_data(url):
    response = requests.get(url)

    response.encoding = 'utf-8'
    html = response.text

    return html
    