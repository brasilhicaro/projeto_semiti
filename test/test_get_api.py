import pytest

import requests


def test_get_api():
    response =  requests.get("http://localhost:8000/")
    assert response.status_code == 200

    