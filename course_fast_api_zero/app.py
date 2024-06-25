from http import HTTPStatus

from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse

from course_fast_api_zero.schemas import (
    Message,
    UserDB,
    UserList,
    UserPublic,
    UserSchema,
)

app = FastAPI()
mock_db = []


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


@app.get('/users/', response_model=UserList)
def get_users():
    return {'users': mock_db}


@app.get('/users/{user_id}', response_model=UserPublic)
def get_user_by_id(user_id: int):
    if user_id > len(mock_db) or user_id < 1:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='User not found'
        )

    user_with_id = mock_db[user_id - 1]
    return user_with_id


@app.post('/users/', status_code=HTTPStatus.CREATED, response_model=UserPublic)
def create_user(user: UserSchema):
    user_with_id = UserDB(id=len(mock_db) + 1, **user.model_dump())

    mock_db.append(user_with_id)

    return user_with_id


@app.put('/users/{user_id}', response_model=UserPublic)
def update_user(user_id: int, user: UserSchema):
    if user_id > len(mock_db) or user_id < 1:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='User not found'
        )

    user_with_id = UserDB(id=user_id, **user.model_dump())
    mock_db[user_id - 1] = user_with_id

    return user_with_id


@app.delete('/users/{user_id}', response_model=Message)
def delete_user(user_id: int):
    if user_id > len(mock_db) or user_id < 1:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='User not found'
        )

    del mock_db[user_id - 1]
    return {'message': 'User deleted'}
