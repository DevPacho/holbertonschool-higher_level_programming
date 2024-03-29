#!/usr/bin/python3
""" Script that takes in a URL, sends a request to the URL and displays the
value of the 'X-Request-Id' variable found in the header of the response."""

from urllib import request
from sys import argv

if __name__ == "__main__":

    URL = argv[1]
    with request.urlopen(URL) as content:
        print(content.headers.get('X-Request-Id'))
