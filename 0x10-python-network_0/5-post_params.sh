#!/bin/bash
# Script that takes in a URL, sends a POST request to the passed URL, and displays the body of the response with some variables.
curl -s "$1" -X POST -d '{"email": "test@gmail.com", "subject": "I will always be here for PLD"}'
