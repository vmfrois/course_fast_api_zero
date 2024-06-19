from http import HTTPStatus

from fastapi.testclient import TestClient

from course_fast_api_zero.app import app


def test_read_root_should_return_Ok():
    client = TestClient(app)

    response = client.get('/')

    assert response.status_code == HTTPStatus.OK


def test_read_root_should_return_hello_world():
    client = TestClient(app)

    response = client.get('/')

    assert response.json() == {'message': 'Hello world!'}


def test_get_hello_world_html():
    client = TestClient(app)

    response = client.get('/hello-world')

    expected_html = """
    <html>
      <head>
        <title> Nosso olá mundo!</title>
      </head>
      <body>
        <h1>olá mundo</h1>
      </body>
    </html>"""

    assert response.text.strip() == expected_html.strip()
