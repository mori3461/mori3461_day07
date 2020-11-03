import os
from pprint import pprint

import requests

def main():
    ACCESS_KEY = os.environ['ACCESS_KEY']
    freeword = 'wine'
    url = f'https://api.gnavi.co.jp/RestSearchAPI/v3/?keyid={ACCESS_KEY}&freeword={freeword}'
    # GETリクエストを送っている
    response = requests.get(url)

    print(response)
    pprint(response.json())


if __name__ == '__main__':
    main()

