#!/usr/bin/python3
'''
    Python script that fetches https://alx-intranet.hbtn.io/status
'''

import requests

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"

    with requests.get(url) as response:
        body = response.content
        print("Body response:")
        print("\t- type:", type(body))
        print("\t- content:", body)