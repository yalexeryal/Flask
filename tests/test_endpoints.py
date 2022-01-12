import os

import requests
import pytest


url = os.getenv('URL')


class TestEndpoits:
    def test_correct_login(self):
        response = requests.get(f'{url}/health')
        assert response.status_code == 200
        assert response.json()["status"] == 'OK'