#!/usr/bin/python3
'''
    Python script that fetches https://alx-intranet.hbtn.io/status
'''

import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    with requests.get(url) as response:
        print(response.headers.get('X-Request-Id'))
