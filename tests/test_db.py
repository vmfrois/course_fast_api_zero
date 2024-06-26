from sqlalchemy import select

from course_fast_api_zero.models import User


def test_create_user(session):
    new_user = User(
        username='testusername', password='password123', email='test@mail.com'
    )

    session.add(new_user)
    session.commit()

    user = session.scalar(select(User).where(User.username == 'testusername'))

    assert user.username == 'testusername'
