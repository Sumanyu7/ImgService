from flask import Flask
from io import BytesIO
import pytest

def test_upload():
    app = Flask(__name__)
    client = app.test_client() 
    data = {
        'file': (BytesIO(b'test'), 'sample.jpeg'), 
    }
    response = client.post("/images", content_type='multipart/form-data', data=data)

    assert response.status_code == 200
    


