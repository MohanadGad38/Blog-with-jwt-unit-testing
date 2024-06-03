from blog import schemas, models
from blog.database import get_db
from sqlalchemy.orm import Session
from typing import List
from fastapi import Depends
from blog.repository import blog
from unittest.mock import MagicMock


def test_get_all():
    # Create a mock database session
    fake_db_session: MagicMock = MagicMock()

    # Create some fake blog data
    fake_blogs: List[MagicMock] = [
        MagicMock(id=1, title="Blog 1", body="Body 1"),
        MagicMock(id=2, title="Blog 2", body="Body 2")
    ]

    # Mock the behavior of the database session to return the fake blog data
    fake_db_session.query.return_value.all.return_value = fake_blogs

    # Call the get_all function with the mocked database session
    result: blog = blog.get_all(db=fake_db_session)
    # Assert that the result matches the fake blog data
    assert result == fake_blogs
