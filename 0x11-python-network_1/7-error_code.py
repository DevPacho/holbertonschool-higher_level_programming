#!/usr/bin/python3
""" Script that takes in a URL, sends a request to the URL
and displays the body of the response (decoded in utf-8).

- Managing urllib.error.HTTPError exceptions and print: Error code: followed by
the HTTP status code.

- With 'requests' package """

import requests
from sys import argv

if __name__ == "__main__":

    response = requests.get(argv[1])
    if response.status_code >= 400:
        print('Error code: {}'.format(response.status_code))
    else:
        print(response.text)