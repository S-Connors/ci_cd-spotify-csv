import unittest
import requests
import os
from dotenv import load_dotenv

load_dotenv()

class TestMainScript(unittest.TestCase):

    def test_read_api(self):
        response = requests.post(os.getenv('url'), {
        'grant_type': 'client_credentials',
        'client_id': os.getenv('client_id'),
        'client_secret': os.getenv('client_secret'),
        })
        self.assertEqual(200, response.status_code)

    def get_headers(self):
        pass

if __name__ == '__main__':
    unittest.main()