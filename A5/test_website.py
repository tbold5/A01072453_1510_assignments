from unittest import TestCase
from q06 import website
from unittest.mock import patch
import requests
import json
import os


class TestWebsite(TestCase):
    @patch('builtins.input', side_effect=['Trae', 'I love python'])
    def test_website_check_name(self, mock_input):
        name = 'Trae'
        website()
        with open('index.html') as f_obj:
            content = f_obj.read()
            self.assertTrue(name in content)

    @patch('builtins.input', side_effect=['Trae', 'I love python'])
    def test_website_check_description(self, mock_input):
        description = 'I love python'
        website()
        with open('index.html') as f_obj:
            content = f_obj.read()
            self.assertTrue(description in content)

    @patch('builtins.input', side_effect=['Trae', 'I love python'])
    def test_website_check_url(self, mock_input):
        my_url = 'https://api.nasa.gov/planetary/apod?api_key=g3Azcc1eRqqKWznqCaEeX7QP3TOSX2mH3KBDRwao'
        response = requests.get(my_url)
        response.raise_for_status()
        info_dictionary = json.loads(response.text)
        website_url = info_dictionary['url']
        website()
        with open('index.html') as f_obj:
            content = f_obj.read()
            self.assertTrue(website_url in content)


    def test_file_exist(self):
        self.assertTrue(os.path.exists("./index.html"))
