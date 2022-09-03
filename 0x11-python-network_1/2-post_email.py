#!/usr/bin/python3
""" Script that takes in a URL and an email, sends a POST request
to the passed URL with the email as a parameter, and displays
the body of the response (decoded in utf-8) """

from urllib import request, parse
from sys import argv

if __name__ == "__main__":

    url = argv[1]
    email = argv[2]
    data_email = parse.urlencode({"email": email}).encode()

    with request.urlopen(request.Request(url), data_email) as content:
        print(content.read().decode())
