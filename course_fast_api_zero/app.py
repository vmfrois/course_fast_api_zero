from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from course_fast_api_zero.schemas import Message

app = FastAPI()


@app.get('/', response_model=Message)
def read_root():
    return {'message': 'Hello world!'}


@app.get('/hello-world', response_class=HTMLResponse)
def get_hello_world_html():
    return """
    <html>
      <head>
        <title> Nosso olá mundo!</title>
      </head>
      <body>
        <h1>olá mundo</h1>
      </body>
    </html>"""
