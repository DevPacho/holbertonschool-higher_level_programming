#!/usr/bin/python3
""" Script that takes in a letter and sends a POST request
to 'http://0.0.0.0:5000/search_user' with the 'letter' as a parameter. """

import requests
from sys import argv

if __name__ == "__main__":

    url = "http://0.0.0.0:5000/search_user"

    if len(argv) == 2:
        letter = argv[1]
        check_args = 0
    else:
        letter = ""
        check_args = 1

    if check_args == 0 and type(letter) is str:
        send_letter = requests.post(url, data={"q": letter})
    elif check_args == 1:
        send_letter = requests.post(url, data={"q": letter})

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
