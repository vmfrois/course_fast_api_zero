import pytest
from fastapi.testclient import TestClient
from sqlalchemy import StaticPool, create_engine
from sqlalchemy.orm import Session

from course_fast_api_zero.app import app
from course_fast_api_zero.database import get_session
from course_fast_api_zero.models import User, table_registry


@pytest.fixture()
def client(session):
    def get_test_session_override():
        return session

    with TestClient(app) as client:
        app.dependency_overrides[get_session] = get_test_session_override

        yield client

    app.dependency_overrides.clear()


@pytest.fixture()
def session():
    engine = create_engine(
        'sqlite:///:memory:',
        connect_args={'check_same_thread': False},
        poolclass=StaticPool,
    )
    table_registry.metadata.create_all(engine)

    with Session(engine) as session:
        yield session

    table_registry.metadata.drop_all(engine)


@pytest.fixture()
def user(session):
    user = User(
        username='Test', email='test@example.com', password='password123'
    )

    session.add(user)
    session.commit()
    session.refresh(user)

    return user
