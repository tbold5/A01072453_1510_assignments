"""COMP1510 Assignment 5: Back to basics"""

# Trae Bold
# A01072453
# JAN 11, 2019

import requests
import json


def website():
    my_url = 'https://api.nasa.gov/planetary/apod?api_key=g3Azcc1eRqqKWznqCaEeX7QP3TOSX2mH3KBDRwao'
    response = requests.get(my_url)
    response.raise_for_status()
    info_dictionary = json.loads(response.text)

    website_url = info_dictionary['url']
    user_name = input('Please enter your name: ').title()
    user_description = input('Please describe yourself in one sentence: ')
    with open('index.html', 'w') as f_obj:
        template = ("<!doctype html>\n<html lang='en'>\n<head>\n<meta charset='utf-8'>\n<title>Introduction</title>\n"
                    "<meta name='description' content=" + user_name + "'s Webpage>\n"
                    "<meta name='author' content=" + user_name + ">\n"
                    "<link rel='stylesheet' href='css/styles.css?v=1.0'></head>\n<body>\n<center>\n<h1>" + user_name + "</h1>\n"
                    "</center>\n" + user_description + "\n<img src = " + website_url + "></img>\n</body>\n</html>\n")
        f_obj.write(template)


def main():
    website()


if __name__ == '__main__':
    main()
