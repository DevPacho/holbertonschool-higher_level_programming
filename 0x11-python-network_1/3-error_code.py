#!/usr/bin/python3
""" Script that takes in a URL, sends a request to the URL
and displays the body of the response (decoded in utf-8).

- Managing urllib.error.HTTPError exceptions and print: Error code: followed by
the HTTP status code. """

from sys import argv
from urllib import request
from urllib.error import HTTPError

if __name__ == "__main__":

    url = argv[1]

    try:
        with request.urlopen(url) as content:
            print(content.read().decode())
    except HTTPError as err:
        print("Error code:", err.code)
