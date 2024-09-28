import sys
import os
import pytest

# 将项目根目录添加到 Python 路径
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_page(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"AI\xe8\x81\x8a\xe5\xa4\xa9\xe5\x8a\xa9\xe6\x89\x8b" in response.data

def test_chat_endpoint(client):
    response = client.post('/chat', json={'message': '你好'})
    assert response.status_code == 200
    assert 'response' in response.json 