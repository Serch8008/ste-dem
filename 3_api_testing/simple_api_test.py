import requests

def test_api():
    r = requests.get('https://jsonplaceholder.typicode.com/posts/1')
    assert r.status_code == 200