#!/usr/bin/python3
""" Script that takes in a letter and sends a POST request
to 'http://0.0.0.0:5000/search_user' with the letter as a parameter. """

import requests
from sys import argv

if __name__ == "__main__":

    letter = argv[1]
    url = "http://0.0.0.0:5000/search_user"

    if len(argv) > 1:
        send_letter = requests.post(url, data={"q": letter})
    else:
        send_letter = requests.post(url, data={"q": ""})

    try:
        json_format = send_letter.json()

        if json_format:
            get_id = json_format.get('id')
            get_name = json_format.get('name')
            print("[{}] {}".format(get_id, get_name))
        else:
            print("No result")
    except Exception:
        print("Not a valid JSON")
