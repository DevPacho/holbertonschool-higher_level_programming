#!/usr/bin/python3
""" Script that fetches 'https://intranet.hbtn.io/status' """

from urllib import request

if __name__ == "__main__":

    URL = "https://intranet.hbtn.io/status"
    with request.urlopen(URL) as content:
        response = content.read()
    print("Body response:")
    print("\t- type:", type(response))
    print("\t- content:", response)
    print("\t- utf8 content:", response.decode())
