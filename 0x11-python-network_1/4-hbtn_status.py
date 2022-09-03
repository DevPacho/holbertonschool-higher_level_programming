#!/usr/bin/python3
""" Script that fetches 'https://intranet.hbtn.io/status'
with requests package """

import requests

if __name__ == "__main__":

    url = "https://intranet.hbtn.io/status"
    response = requests.get(url)
    to_str = str(response)

    print("Body response:")
    print("\t- type:", type(to_str))
    print("\t- content:", response.text)
