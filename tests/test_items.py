import pytest
import requests

def test_add_items():
    url = 'http://127.0.0.1:8000/api/users/'
    response = requests.get(url)
    print(response.text)
    assert response.status_code == 200
